---
type: prompt_template
status: ready
routing_engine: python_script
routing_provider: together
routing_model: "moonshotai/Kimi-K2.6"
routing_api_key_env_var: TOGETHER_API_KEY
routing_base_url: "https://api.together.ai/v1"
---

# YAML Property Options

This note uses flat YAML properties for Obsidian compatibility. The routing fields define whether the prompt is executed through a Python script using the Together API or through an agentic/chat-based workflow.

| YAML field | Accepted option(s) | Use when | Notes |
|---|---|---|---|
| `type` | `prompt_template` | The note is a reusable prompt template. | Keep fixed unless the note is reclassified. |
| `status` | `draft`, `ready`, `active`, `archived` | Tracks the lifecycle state of the prompt. | Use `ready` when the prompt is validated and executable. |
| `routing_engine` | `python_script`, `antigravity_agent` | Selects the execution route. | `python_script` means the prompt is run through external code; `antigravity_agent` means the prompt is executed directly by the AI agent. |
| `routing_provider` | `together`, `gemini` | Selects the model provider. | Use `together` with scripted API execution; use `gemini` with Antigravity or direct agent orchestration. |
| `routing_model` | Model identifier string | Selects the model used to execute the prompt. | Example: `"moonshotai/Kimi-K2.6"`. Keep the value quoted. |
| `routing_api_key_env_var` | Environment variable name | Points to the API key used by scripted execution. | Example: `TOGETHER_API_KEY`. Never paste the actual API key here. |
| `routing_base_url` | API endpoint URL | Defines the API endpoint for scripted execution. | Example: `"https://api.together.ai/v1"`. Keep URLs quoted. |

## Canonical Routing Profiles

| Profile | `routing_engine` | `routing_provider` | Typical use |
|---|---|---|---|
| Together Python route | `python_script` | `together` | Batch execution, registry-driven prompts, reproducible automation. |
| Antigravity agent route | `antigravity_agent` | `gemini` | Direct agent execution inside Antigravity/chat environments. |

## Canonical YAML Example

```yaml
---
type: prompt_template
status: ready
routing_engine: python_script
routing_provider: together
routing_model: "moonshotai/Kimi-K2.6"
routing_api_key_env_var: TOGETHER_API_KEY
routing_base_url: "https://api.together.ai/v1"
---
```


# TEMPLATE: Prompt Model Choosing and Routing

This template serves as a structural blueprint for defining LLM prompts in this vault. The YAML frontmatter metadata above defines how a prompt should be processed: either programmatically routed via local Python scripts (for Together.ai models) or executed directly by your **Antigravity AI Agent** within the workspace context (bypassing python scripts and not requiring any Gemini API keys).

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
You are a critical literature synthesis assistant for the COMPOL Digital Capitalism project. 
[Insert detailed system instructions and extraction goals here]
```

### Context and Payload Placeholder
```markdown
Below are the source materials to process:
{{payload}}
```

---

## 🐍 Python Implementation Blueprint (Together.ai / Script-based)

Python scripts in `src/notebooklm/` will check the `engine` property. If set to `antigravity_agent` / `gemini`, the script should skip local execution or output an instruction to run it in chat.

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
