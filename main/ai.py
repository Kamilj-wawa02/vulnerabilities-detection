import json
import requests
import os
from time import sleep


MODEL = "meta-llama/llama-3.2-3b-instruct:free" # from: https://openrouter.ai/models
START_INDEX = 0
END_INDEX = 3 # -1
STRATEGY = "zero_shot"  # options: "zero_shot", "role_based"

ZERO_SHOT_PROMPT_BEGINNING = (
    "Examine the following code snippet and determine whether it contains a security vulnerability."
    "If it does, specify the type of vulnerability and indicate its exact location in the code."
    "If it does not, answer 'No vulnerability detected'."
    "Code snippet:"
)

ROLE_BASED_PROMPT_BEGINNING = (
    "You are a senior security specialist with 20 years of experience in detecting and analyzing vulnerabilities in C/C++ applications."
    "Your task is to perform a security audit of the following code snippet."
    "If a vulnerability exists, clearly specify the type of vulnerability and indicate its exact location in the code."
    "If no vulnerability exists, respond with: \"No vulnerability detected\"."
    "Code snippet:"
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


def sort_tests_alphabetically(tests):
    return sorted(tests, key=lambda t: t["name"])


def build_prompt(entry):
    if STRATEGY == "zero_shot":
        beginning = ZERO_SHOT_PROMPT_BEGINNING
    elif STRATEGY == "role_based":
        beginning = ROLE_BASED_PROMPT_BEGINNING

    return beginning + entry["code"]


# def send_request(prompt, api_key):
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": MODEL,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [{"type": "text", "text": prompt}]
#             }
#         ]
#     }

#     response = requests.post(url=API_URL, headers=headers, json=payload)

#     if response.status_code != 200:
#         raise RuntimeError(f"API error {response.status_code}: {response.text}")

#     return response.json()


def send_request(prompt, api_key):
    print("Mock send_request called.")
    # print(prompt)

    return {
        "id": "test-id",
        "object": "chat.completion",
        "created": 1234567890,
        "model": MODEL,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": "No vulnerability detected."}]
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 10,
            "total_tokens": 110
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
    tests = sort_tests_alphabetically(tests)

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

        sleep(0.5)
    
    print("\n\nFinished!")
