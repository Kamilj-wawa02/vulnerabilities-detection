import os
import json
from typing import Dict, Any

RESULTS_DIR = "results-gpt-5.1"
# RESULTS_DIR = "results-grok-code-fast-1"

BENCHMARK_JSON_PATH = "../data/CASTLE-C250.json"

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
        
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            results[base_case_name] = {}
            continue

        results[base_case_name] = parsed

    return results


def evaluate(true_values: Dict[str, Dict[str, Any]], predictions: Dict[str, Dict[str, Any]]):
    TP = TN = FP = FN = 0
    total = 0

    for name, true_data in true_values.items():
        if name not in predictions:
            print(f"No prediction for: {name} (missing file?)")
            continue

        predicted = predictions[name]
        total += 1

        if not "vulnerable" in predicted or not "cwe" in predicted:
            print(f"Incomplete prediction or wrong format at {name} -> predicted: {predicted}")
            continue

        true_v = true_data["vulnerable"]
        true_cwe = true_data["cwe"]
        pred_v = predicted["vulnerable"]
        pred_cwe = predicted["cwe"]

        if pred_v and true_v and pred_cwe != true_cwe:
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

    return {
        "TP": TP,
        "TN": TN,
        "FP": FP,
        "FN": FN,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "total": total
    }


if __name__ == "__main__":
    true_values = load_true_values()
    pred = load_model_results()

    metrics = evaluate(true_values, pred)

    print(f"\n=== Results for {RESULTS_DIR.replace('results-', '')} ===")
    for k, v in metrics.items():
        print(f"{k}: {v}")