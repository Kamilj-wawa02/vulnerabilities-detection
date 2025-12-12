import importlib
from typing import List, Dict

cm = importlib.import_module("calculate_metrics")

FIELDS = [
    "TP", "TN", "FP", "FN",
    "precision", "recall", "f1",
    # "total",
    "correct_format_responses",
    "wrong_format_responses",
    "total_prompt_tokens",
    "total_completion_tokens",
    "total_tokens",
    "total_cost",
    "average_cost_per_sample"
]

RESULTS_DIRECTORIES = [
    "zero_shot/results-gpt-5.1",
    "zero_shot/results-grok-code-fast-1",
    "zero_shot/results-claude-sonnet-4.5",
    "role_based/results-gpt-5.1",
    "role_based/results-grok-code-fast-1",
    "role_based/results-claude-sonnet-4.5"
]

def format_metrics_row(model_name: str, metrics: Dict[str, float], fields: List[str]) -> str:
    row = [model_name]
    for key in fields:
        value = metrics.get(key, "")
        if isinstance(value, float):
            if key in ["average_cost_per_sample"]:
                value = f"{value:.4f}"
            else:
                value = f"{value:.3f}"
        row.append(str(value))
    return "| " + " | ".join(row) + " |"


def print_markdown_table_header(fields: List[str]):
    header = "| Model | " + " | ".join(fields) + " |"
    separator = "|" + "------|" * (len(fields) + 1)
    print(header)
    print(separator)


if __name__ == "__main__":
    print_markdown_table_header(FIELDS)

    cm.LOG_ERRORS = False
    for results_dir in RESULTS_DIRECTORIES:
        cm.RESULTS_DIR = results_dir
        MODEL_NAME = results_dir.replace("results-", "")
        
        true_values = cm.load_true_values()
        predictions = cm.load_model_results()

        metrics_with_cwe_check = cm.evaluate(true_values, predictions, check_cwe=True)
        metrics_without_cwe_check = cm.evaluate(true_values, predictions, check_cwe=False)

        print(format_metrics_row(MODEL_NAME + " (with CWE)", metrics_with_cwe_check, FIELDS))
        print(format_metrics_row(MODEL_NAME + " (without CWE)", metrics_without_cwe_check, FIELDS))