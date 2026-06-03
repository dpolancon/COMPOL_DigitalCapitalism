"""API client for Together.ai using Qwen models."""

import os
import time
import logging
from typing import Optional, Dict, Any
from pathlib import Path

import pandas as pd
from openai import OpenAI
from PyPDF2 import PdfReader
import pdfplumber

logger = logging.getLogger(__name__)


class TogetherAIClient:
    """Wrapper class for Together.ai API interactions."""
    
    def __init__(self, base_url: str = "https://api.together.ai/v1", api_key: Optional[str] = None):
        """Initialize the TogetherAI client.
        
        Args:
            base_url: The base URL for the Together.ai API
            api_key: The API key for authentication. If None, will be loaded from environment.
        """
        if api_key is None:
            api_key = os.getenv("OPEN_API_KEY")
            if not api_key:
                raise ValueError("API key must be provided or set in OPEN_API_KEY environment variable")
        
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )
    
    def extract_text(self, pdf_path: str, max_pages: int = 5) -> str:
        """Extract text from the first pages of a PDF.
        
        Args:
            pdf_path: Path to the PDF file
            max_pages: Maximum number of pages to extract (default: 5)
            
        Returns:
            Extracted text from the PDF
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        text = ""
        try:
            # Try pdfplumber first (better for complex layouts)
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages[:max_pages]):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {i+1} ---\n{page_text}\n"
        except Exception as e:
            logger.warning(f"pdfplumber failed, falling back to PyPDF2: {e}")
            # Fallback to PyPDF2
            with open(pdf_path, "rb") as file:
                reader = PdfReader(file)
                for i, page in enumerate(reader.pages[:max_pages]):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {i+1} ---\n{page_text}\n"
        
        return text.strip()
    
    def query_llm(self, prompt_text: str, model: str = "Qwen/Qwen3.5-9B", max_retries: int = 3) -> str:
        """Send a prompt to the LLM and return the response.
        
        Args:
            prompt_text: The prompt to send to the model
            model: The model to use (default: Qwen/Qwen3.5-9B)
            max_retries: Maximum number of retry attempts for rate limits
            
        Returns:
            The model's response as a string
            
        Raises:
            Exception: If the API call fails after all retries
        """
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt_text}
                    ],
                    temperature=0.7,
                    max_tokens=8192,
                )
                return response.choices[0].message.content.strip()
            
            except Exception as e:
                if "rate limit" in str(e).lower() and attempt < max_retries - 1:
                    # Exponential backoff for rate limits
                    wait_time = (2 ** attempt) + 1  # 2, 5, 9 seconds
                    logger.warning(f"Rate limit hit. Waiting {wait_time} seconds before retry {attempt + 1}/{max_retries}")
                    time.sleep(wait_time)
                else:
                    logger.error(f"API call failed after {attempt + 1} attempts: {e}")
                    raise e
        
        raise Exception("Max retries exceeded")