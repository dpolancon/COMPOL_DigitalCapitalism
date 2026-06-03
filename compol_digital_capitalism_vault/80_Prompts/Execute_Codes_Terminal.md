
### 💡 How to execute this in your terminal:

1. Save the markdown block above as `PROMPT_03_CODE_GENERATION_PIPELINE.md` in your `80_Prompts` folder.
2. Open your `qwen` terminal.
3. Fire the execution prompt, followed by the new prompt, and **crucially**, attach the legacy scripts folder so the AI can refactor them:

```text
@C:\ReposGitHub\COMPOL_DigitalCapitalism\compol_digital_capitalism_vault\80_Prompts\PROMPT_02_EXECUTE_EXTERNAL_PROMPT.md
@C:\ReposGitHub\COMPOL_DigitalCapitalism\compol_digital_capitalism_vault\80_Prompts\PROMPT_03_CODE_GENERATION_PIPELINE.md
@C:\ReposGitHub\COMPOL_DigitalCapitalism\src\notebooklm\old_scripts
```

_(Note: If your terminal doesn't support folder `@` mentions, list the specific `.py` files inside `old_scripts` instead)._

### What happens next?

The terminal AI will read the legacy code, understand the exact Excel columns and YAML schema I embedded in the prompt, and output the complete, modular Python code for `api.py` and `extract_literature.py`.

Once it generates the report, you can save it to `81_Outputs`, copy the code blocks into your actual repository files, and you will have a fully functional, cost-optimized LLM extraction pipeline ready to test on the first GREEN row of your registry!