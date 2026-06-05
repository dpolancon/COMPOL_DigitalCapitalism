---
type: prompt_template
status: ready
routing_engine: python_script
routing_provider: together
routing_model: "moonshotai/Kimi-K2.6"
routing_api_key_env_var: TOGETHER_API_KEY
routing_base_url: "https://api.together.ai/v1"
---

## 🛠️ Routing Configuration Guide

The `routing` block in the YAML frontmatter controls the execution route:

### Option A: Together.ai API Route (via Python script)
This route is utilized when you want to run batch or structured programmatic scripts locally in the background. It requires a Together.ai API key.
*   `engine`: Set to `python_script`
*   `provider`: Set to `together`
*   `model`: Set to a Together.ai serverless identifier (e.g., `moonshotai/Kimi-K2.6`, `meta-llama/Llama-3.3-70B-Instruct-Turbo`)
*   `api_key_env_var`: Set to `TOGETHER_API_KEY` (or `OPEN_API_KEY` depending on `.env` configurations)
*   `base_url`: Set to `https://api.together.ai/v1`

### Option B: Antigravity Agent Route (Gemini Native)
This route is used when you want the **Antigravity AI Agent** to execute the prompt directly in your chat environment.
*   `engine`: Set to `antigravity_agent`
*   `provider`: Set to `gemini`
*   `model`: `gemini-pro` / `gemini-ultra` (indicates the agent workspace preference)
*   `api_key_env_var`: `None` (not required)

> [!IMPORTANT]
> **No API Key Required for Gemini/Antigravity**
> Under **Option B**, you do **not** need to provide, enable, or configure a Gemini API key. Since Antigravity is natively integrated into your workspace environment with your Gemini account, you can simply point Antigravity to this prompt file (e.g., using `@file` mentions) and instruct the agent to run it. Antigravity will parse the prompt and execute it directly.

---

## 📝 Prompt Content Section

Add the actual prompt structure here.

### System Instructions
```markdown
You are an expert academic co-author and critical literature synthesis assistant specializing in political communication, digital capitalism, and Latin American politics (specifically the 2021 Chilean elections).

  

Your task is to synthesize the provided conceptual framework spine and literature notes into a cohesive, highly structured first-pass draft.

  

**CRITICAL FORMATTING RULES:**

For every paragraph you generate, you MUST strictly follow this exact three-part structure without deviation:

  

1. **Paragraph Title:** A concise, bolded title summarizing the paragraph's core argument or theoretical construct.

2. _Functional Explanation:_ A single sentence in italics explaining the rhetorical purpose of the paragraph (e.g., what gap it fills, what debate it intervenes in, or what theoretical construct it operationalizes).

3. > First-Pass Draft: The actual academic text of the paragraph, formatted as a markdown blockquote (`>`).

  

**CONTENT & POSITIONING RULES:**

- **Embedded Positioning:** Do not just summarize the literature (e.g., avoid "Author A says X, Author B says Y"). Instead, actively use the literature to position the research. Highlight debates, identify methodological or theoretical blind spots (e.g., the over-focus on ad copy vs. metadata), and explicitly justify how this research fills those gaps.

- **Contextual Grounding:** Always anchor arguments in the specific context of the 2021 Chilean elections (post-*estallido social*, institutional crisis, constitutional process). Avoid generic statements about "the digital age" or "social media changing politics."

- **Tone:** Formal, analytical, and grounded in critical political economy and heterodox macroeconomics. Avoid techno-determinism.

- **Citations:** Use strict APA 7th edition format for all in-text citations. Only cite authors and works provided in the source materials.

  

**EXAMPLE OF EXPECTED OUTPUT FORMAT:**

  

**The North American Baseline: Psychographics and the "Emphasis" Paradigm**

_This paragraph establishes the dominant Global North definition of microtargeting, contrasting dystopian fears with the pragmatic "emphasis" paradigm to define the baseline terminology of the field._

> The study of digital political communication in the Global North has largely coalesced around two competing definitions of microtargeting. On one hand, a critical strand of literature conceptualizes it as a mechanism of behavioral manipulation, wherein campaigns utilize granular psychographic data to deliver fragmented messages (Gorton, 2016; Hersh, 2015). Conversely, a more pragmatic tradition argues that microtargeting is primarily an "emphasis" tool rather than a deception tool, constrained by campaign budgets (Kreiss, 2016). Establishing this baseline is crucial, as it highlights a field preoccupied with the *content* of the ads, often overlooking the underlying political economy of the platforms that facilitate this targeting.
```

### Context and Payload Placeholder
```markdown
Below are the source materials (Conceptual Framework spine, Literature Clusters, and Paper Notes) to process. Synthesize these into the structured first-pass draft following the exact formatting rules above.

{{payload}}
```

---

## 🐍 Python Implementation Blueprint (Together.ai / Script-based)

When your Python script in `src/notebooklm/` executes this prompt:

1. It will parse the YAML and identify `routing_engine: python_script` and `routing_model: "moonshotai/Kimi-K2.5"`.
2. It will load the `TOGETHER_API_KEY` from your environment.
3. It will concatenate the **System Instructions** and the **Context** block.
4. It will replace `{{payload}}` with the flattened text of your transcluded `![[wikilinks]]` (your `02_ConceptualFramework.md` spine + relevant `CF` and `NB` cluster notes).
5. It will send the final compiled prompt to `https://api.together.ai/v1` and stream/save the response.

Here is a recommended script snippet:

```python
import os
import yaml
from pathlib import Path
from openai import OpenAI

def process_prompt_routing(prompt_file_path: Path, payload_content: str):
    """Checks the routing header. If python_script, executes it; if antigravity_agent, prompts manual agent execution."""
    content = prompt_file_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        raise ValueError("Note is missing YAML frontmatter.")
        
    parts = content.split('---', 2)
    metadata = yaml.safe_load(parts[1])
    prompt_body = parts[2].strip()
    
    routing = metadata.get("routing", {})
    engine = routing.get("engine", "python_script")
    provider = routing.get("provider", "together")
    
    if engine == "antigravity_agent" or provider == "gemini":
        print(f"\n[AGENT ROUTE DETECTED]")
        print(f"This prompt is configured for direct execution via your Antigravity agent.")
        print(f"Please ask Antigravity in chat to run the prompt: {prompt_file_path.name}")
        return None
        
    # Programmatic execution for Together API
    model = routing.get("model")
    api_key_var = routing.get("api_key_env_var", "TOGETHER_API_KEY")
    api_key = os.getenv(api_key_var)
    
    if not api_key:
        raise ValueError(f"Together API key not found in env variable: {api_key_var}")
        
    client = OpenAI(
        base_url=routing.get("base_url", "https://api.together.ai/v1"),
        api_key=api_key
    )
    
    full_prompt = prompt_body.replace("{{payload}}", payload_content)
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response.choices[0].message.content.strip()
```
