import requests
import json

MODEL = "meta-llama/llama-3.2-3b-instruct:free"

API_URL = "https://openrouter.ai/api/v1/chat/completions"
CONFIG_PATH = "../config.json"

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)
API_KEY = config.get("OPENROUTER_API_KEY")

if not API_KEY:
    print("No OPENROUTER_API_KEY!")
    exit(1)

headers = {
    "Authorization": f'Bearer {API_KEY}',
    "Content-Type": "application/json"
}

payload = json.dumps({
    "model": MODEL,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is the meaning of life?"
          }
        ]
      }
    ]
})

response = requests.post(url=API_URL, headers=headers, data=payload)
result = response.json()
print(json.dumps(result, indent=2))
