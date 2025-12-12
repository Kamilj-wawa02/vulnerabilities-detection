import os
import json
from typing import Dict, Any

# RESULTS_DIR = "zero_shot/results-gpt-5.1"
# RESULTS_DIR = "zero_shot/results-grok-code-fast-1"
# RESULTS_DIR = "zero_shot/results-claude-sonnet-4.5"

# RESULTS_DIR = "role_based/results-gpt-5.1"
# RESULTS_DIR = "role_based/results-grok-code-fast-1"
RESULTS_DIR = "role_based/results-claude-sonnet-4.5"

BENCHMARK_JSON_PATH = "../data/CASTLE-C250.json"
LOG_ERRORS = True


def load_true_values() -> Dict[str, Dict[str, Any]]:
    with open(BENCHMARK_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    true_values = {}
    for test in data["tests"]:
        true_values[test["name"]] = {
            "vulnerable": test["vulnerable"],
            "cwe": test["cwe"]
        }
    return true_values


def load_model_results() -> Dict[str, Dict[str, Any]]:
    results = {}

    for file in os.listdir(RESULTS_DIR):
        if not file.endswith(".json") or not file.startswith("CASTLE-"):
            continue

        filepath = os.path.join(RESULTS_DIR, file)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        base_case_name = file.replace(".json", "") # e.g. "CASTLE-22-1.c"

        content = data["choices"][0]["message"]["content"]
        content = content.replace("```json\n", "").replace("```", "")
        
        prompt_tokens = data["usage"]["prompt_tokens"]
        completion_tokens = data["usage"]["completion_tokens"]
        total_tokens = data["usage"]["total_tokens"]
        cost = data["usage"]["cost"]

        try:
            parsed_content = json.loads(content)
        except json.JSONDecodeError:
            results[base_case_name] = {}
            continue

        results[base_case_name] = {
            "content": parsed_content,
            "usage": {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "cost": cost
            }
        }

    return results


def evaluate(true_values: Dict[str, Dict[str, Any]], predictions: Dict[str, Dict[str, Any]], check_cwe: bool = True) -> Dict[str, Any]:
    TP = TN = FP = FN = 0
    total = 0
    correct_format_responses = 0
    wrong_format_responses = 0

    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_tokens = 0
    total_cost = 0.0

    for name, true_data in true_values.items():
        if name not in predictions:
            if LOG_ERRORS:
                print(f"No prediction for: {name} (missing file?)")
            continue

        predicted = predictions[name]
        total += 1

        content = predicted.get("content", {})

        total_prompt_tokens += predicted.get("usage", {}).get("prompt_tokens", 0)
        total_completion_tokens += predicted.get("usage", {}).get("completion_tokens", 0)
        total_tokens += predicted.get("usage", {}).get("total_tokens", 0)
        total_cost += predicted.get("usage", {}).get("cost", 0.0)

        if not "vulnerable" in content or not "cwe" in content:
            if LOG_ERRORS:
                print(f"Incomplete prediction or wrong format at {name} -> predicted: {predicted}")
            wrong_format_responses += 1
            continue

        correct_format_responses += 1

        true_v = true_data["vulnerable"]
        true_cwe = true_data["cwe"]
        pred_v = content["vulnerable"]
        pred_cwe = content["cwe"]

        if check_cwe and (pred_v and true_v and pred_cwe != true_cwe):
            pred_v = False

        if pred_v and true_v:
            TP += 1
        elif not pred_v and not true_v:
            TN += 1
        elif pred_v and not true_v:
            FP += 1
        elif not pred_v and true_v:
            FN += 1

    precision = TP / (TP + FP) if (TP + FP) else 0
    recall = TP / (TP + FN) if (TP + FN) else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
    average_cost = total_cost / total if total else 0.0

    return {
        "TP": TP,
        "TN": TN,
        "FP": FP,
        "FN": FN,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "total": total,
        "correct_format_responses": correct_format_responses,
        "wrong_format_responses": wrong_format_responses,
        "total_prompt_tokens": total_prompt_tokens,
        "total_completion_tokens": total_completion_tokens,
        "total_tokens": total_tokens,
        "total_cost": total_cost,
        "average_cost_per_sample": average_cost
    }


if __name__ == "__main__":
    true_values = load_true_values()
    pred = load_model_results()

    metrics_with_cwe_check = evaluate(true_values, pred, check_cwe=True)
    LOG_ERRORS = False
    metrics_without_cwe_check = evaluate(true_values, pred, check_cwe=False)

    print(f"\n=== Results for {RESULTS_DIR.replace('results-', '')} (with CWE check) ===")
    for k, v in metrics_with_cwe_check.items():
        print(f"{k}: {v}")
    
    print(f"\n=== Results for {RESULTS_DIR.replace('results-', '')} (without CWE check) ===")
    for k, v in metrics_without_cwe_check.items():
        print(f"{k}: {v}")