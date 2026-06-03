import os
from src.notebooklm.api import TogetherAIClient

# Load env file manually for simple run
with open('.env') as f:
    for line in f:
        if '=' in line:
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

client = TogetherAIClient()
resp = client.query_llm('Say hello in exactly 5 words.', model='Qwen/Qwen3.5-9B')
print('RESPONSE TYPE:', type(resp))
print('RESPONSE LENGTH:', len(resp) if resp else 0)
print('RESPONSE:')
print(repr(resp))
