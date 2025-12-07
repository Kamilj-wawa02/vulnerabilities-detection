import json
import requests
import os
from time import sleep

# --- Used models: ---
# openai/gpt-5.1
# x-ai/grok-code-fast-1
#
# --- For testing purposes: ---
# openai/gpt-oss-20b:free
# meta-llama/llama-3.2-3b-instruct:free
#
# Models available at: https://openrouter.ai/models

MODEL = "x-ai/grok-code-fast-1"
START_INDEX = 0
END_INDEX = -1
STRATEGY = "role_based"  # options: "zero_shot", "role_based"

DEBUG = False
DEBUG_PROMPTS = False

JSON_FORMAT_REQUIREMENT = """
Return ONLY a JSON object in the following format, and nothing else:
{
  "vulnerable": true or false,
  "cwe": CODE_NUMBER
}
"""

ZERO_SHOT_PROMPT_BEGINNING = (
    "Examine the following code snippet and determine whether it contains a security vulnerability."
)

ROLE_BASED_PROMPT_BEGINNING = (
    "You are a senior security specialist with 20 years of experience in detecting and analyzing vulnerabilities in C/C++ applications. "
    "Review the following code snippet to identify potential vulnerabilities."
)

BENCHMARK_JSON_PATH = "../data/CASTLE-C250.json"
OUTPUT_DIR = "results"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
CONFIG_PATH = "../config.json"


def load_api_key():
    with open(CONFIG_PATH, "r") as f:
        cfg = json.load(f)
    return cfg.get("OPENROUTER_API_KEY")


def load_benchmark():
    with open(BENCHMARK_JSON_PATH, "r") as f:
        return json.load(f)["tests"]


def sort_tests(tests):
    def extract_numbers(name):
        parts = name.split('-')
        return [int(part) for part in parts if part.isdigit()]

    return sorted(tests, key=lambda t: extract_numbers(t["name"]))


def build_prompt(entry):
    if STRATEGY == "zero_shot":
        beginning = ZERO_SHOT_PROMPT_BEGINNING
    elif STRATEGY == "role_based":
        beginning = ROLE_BASED_PROMPT_BEGINNING

    return beginning + JSON_FORMAT_REQUIREMENT + "\nCode snippet:\n" + entry["code"]


def send_request(prompt, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }
        ]
    }

    if DEBUG:
        return debug_prompt(prompt)
    else:
        response = requests.post(url=API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            raise RuntimeError(f"API error {response.status_code}: {response.text}")
        
        return response.json()


def debug_prompt(prompt):
    if DEBUG_PROMPTS:
        print(f'[DEBUG] Prompt: \n{prompt}')
    return {
        "id": "ID",
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "RESULT"
                }
            }
        ],
        "usage": {
            "prompt_tokens": 690,
            "completion_tokens": 599,
            "total_tokens": 1289,
            "cost": 0
        }
    }


def save_result(test_entry, result):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, f"{test_entry['name']}.json")

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Saved: {out_path}")


if __name__ == "__main__":
    api_key = load_api_key()
    if not api_key:
        print("No OPENROUTER_API_KEY!")
        exit(1)

    tests = load_benchmark()
    tests = sort_tests(tests)

    total = len(tests)
    start = max(0, START_INDEX)
    end = min(END_INDEX if END_INDEX != -1 else total, total)
    total_to_run = end - start

    print(f"Running tests with indexes from {start} to {end - 1} (inclusive) of {total} total tests")

    for idx in range(start, end):
        test_entry = tests[idx]

        prompt = build_prompt(test_entry)

        print(f"\n=== Testing {test_entry['name']} ({idx - start + 1}/{total_to_run}) ===")

        try:
            result = send_request(prompt, api_key)

        except Exception as e:
            print("\nERROR — stopping further tests!")
            print(str(e))
            exit(1)

        save_result(test_entry, result)
    
    print("\n\nFinished!")
