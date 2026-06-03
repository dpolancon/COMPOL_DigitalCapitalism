---
name: Modular LLM Pipeline Development
description: Building modular Python applications for LLM-based text processing pipelines with clean architecture
source: auto-skill
extracted_at: '2026-06-02T17:21:05.066Z'
---

# Modular LLM Pipeline Development

This skill describes how to build modular Python applications for LLM-based text processing pipelines following clean architecture principles.

## Approach

1. **Modular Design**:
   - Separate concerns into distinct modules (API clients, utilities, main processing logic)
   - Create a main CLI entry point that orchestrates the workflow
   - Use helper modules for specific functions like environment loading and text processing

2. **API Client Design**:
   - Create wrapper classes for external APIs with proper error handling
   - Implement retry mechanisms with exponential backoff for rate limits
   - Provide fallback mechanisms for critical operations (e.g., PDF text extraction)

3. **Main Processing Logic**:
   - Implement a clear data flow: load data → filter → process → save → update status
   - Use pandas for data manipulation when working with structured data like Excel files
   - Include comprehensive logging for debugging and monitoring

4. **Utility Functions**:
   - Create helper functions for common operations like environment variable loading
   - Implement validation functions for data integrity checks
   - Use configuration patterns for prompt templates and other static data

5. **Error Handling**:
   - Implement try/except blocks around critical operations
   - Use logging to track both successes and failures
   - Design graceful degradation when possible (e.g., fallback PDF extraction methods)

6. **CLI Interface**:
   - Use argparse for command-line argument parsing
   - Provide sensible defaults for optional parameters
   - Include help text for all arguments

## Implementation Pattern

1. **api.py**:
   - Contains API client classes with methods for specific operations
   - Handles authentication and connection management
   - Implements retry logic for unreliable network operations

2. **extract_literature.py** (or similar main module):
   - Serves as the CLI entry point
   - Orchestrates the main processing workflow
   - Handles data loading, filtering, and saving
   - Updates source status tracking

3. **utils.py**:
   - Contains helper functions for common operations
   - Implements data validation and transformation functions
   - Stores configuration data and prompt templates

4. **__init__.py**:
   - Makes the directory a proper Python package
   - Can expose key classes/functions for easier imports

## Best Practices

- Use type hints for better code documentation and IDE support
- Write comprehensive docstrings for all functions and classes
- Implement logging instead of print statements for better debugging
- Handle file paths using pathlib for cross-platform compatibility
- Use environment variables for sensitive configuration data
- Include proper error messages that help with debugging
- Design for extensibility by separating configuration from logic