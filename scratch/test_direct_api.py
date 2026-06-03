import os
import requests

with open('.env') as f:
    for line in f:
        if '=' in line:
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

api_key = os.environ.get("OPEN_API_KEY")
url = "https://api.together.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "Qwen/Qwen3.5-9B",
    "messages": [
        {"role": "user", "content": "Say hello in exactly 5 words."}
    ],
    "temperature": 0.7
}

resp = requests.post(url, json=payload, headers=headers)
print("STATUS CODE:", resp.status_code)
print("RESPONSE TEXT:")
print(resp.text)
