import importlib
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

cm = importlib.import_module("calculate_metrics")
cm.LOG_ERRORS = False

PROMPTING_STRATEGIES = {
    "Zero-shot": [
        "zero_shot/results-gpt-5.1",
        "zero_shot/results-grok-code-fast-1",
        "zero_shot/results-claude-sonnet-4.5",
        "zero_shot/results-devstral-2512",
    ],
    "Role-based": [
        "role_based/results-gpt-5.1",
        "role_based/results-grok-code-fast-1",
        "role_based/results-claude-sonnet-4.5",
        "role_based/results-devstral-2512",
    ],
    "Chain-of-thought": [
        "chain_of_thought/results-grok-code-fast-1",
        "chain_of_thought/results-devstral-2512",
    ],
}

PROMPTING_STRATEGIES_MODEL_ORDER = [
    "gpt-5.1",
    "grok-code-fast-1",
    "claude-sonnet-4.5",
    "devstral-2512",
]

PROMPTING_STRATEGIES_COLORS = {
    "Zero-shot": "tab:blue",
    "Role-based": "tab:green",
    "Chain-of-thought": "tab:cyan",
}

TEMPERATURE_EXPERIMENTS = {
    "0.5": [
        "temperatures/zero_shot/0.5/results-gpt-5.1",
        "temperatures/zero_shot/0.5/results-devstral-2512",
    ],
    "1.0": [
        "zero_shot/results-gpt-5.1",
        "zero_shot/results-devstral-2512",
    ],
    "1.5": [
        "temperatures/zero_shot/1.5/results-gpt-5.1",
        "temperatures/zero_shot/1.5/results-devstral-2512",
    ],
}

TEMPERATURE_EXPERIMENTS_MODEL_ORDER = [
    "devstral-2512",
    "gpt-5.1"
]

MODEL_COLORS = {
    "gpt-5.1": (16/255, 163/255, 127/255),          # OpenAI – teal
    "grok-code-fast-1": (0/255, 0/255, 0/255),      # xAI – black
    "claude-sonnet-4.5": (255/255, 165/255, 0/255), # Anthropic – orange
    "devstral-2512": (128/255, 0/255, 128/255),     # Mistral/Devstral – purple
}


def darken(color, factor=0.8):
    return tuple(max(0, c * factor) for c in color)


def lighten(color, factor=1.2):
    return tuple(min(1, c * factor) for c in color)


def compute_f1(results_dir: str, use_cwe_check: bool = True) -> float:
    cm.RESULTS_DIR = results_dir
    true_values = cm.load_true_values()
    predictions = cm.load_model_results()
    metrics = cm.evaluate(true_values, predictions, check_cwe=use_cwe_check)
    return metrics["f1"]


def model_name_from_dir(path: str) -> str:
    return os.path.basename(path).replace("results-", "")


def generate_strategy_chart():
    strategies = list(PROMPTING_STRATEGIES.keys())
    models = [
        m for m in PROMPTING_STRATEGIES_MODEL_ORDER
        if any(
            m == model_name_from_dir(d)
            for dirs in PROMPTING_STRATEGIES.values()
            for d in dirs
        )
    ]

    f1_scores = defaultdict(dict)
    for strategy, dirs in PROMPTING_STRATEGIES.items():
        for d in dirs:
            model = model_name_from_dir(d)
            f1_scores[strategy][model] = compute_f1(d)

    x = np.arange(len(models))
    width = 0.25

    plt.figure()

    for i, strategy in enumerate(strategies):
        values = [f1_scores[strategy].get(m, 0) for m in models]
        plt.bar(
            x + i * width,
            values,
            width,
            label=strategy,
            color=PROMPTING_STRATEGIES_COLORS.get(strategy, "gray")
        )

    plt.xticks(x + width, models, rotation=30, ha="right")
    plt.ylabel("F1 score")
    plt.xlabel("Model")
    plt.title("F1 score comparison across prompting strategies")
    plt.legend()
    plt.tight_layout()


def generate_temperature_chart():
    temperatures = ["0.5", "1.0", "1.5"]

    models = [
    m for m in TEMPERATURE_EXPERIMENTS_MODEL_ORDER
        if any(
            m == model_name_from_dir(d)
            for dirs in TEMPERATURE_EXPERIMENTS.values()
            for d in dirs
        )
    ]


    f1_scores = defaultdict(dict)
    for temp, dirs in TEMPERATURE_EXPERIMENTS.items():
        for d in dirs:
            model = model_name_from_dir(d)
            f1_scores[temp][model] = compute_f1(d)

    x = np.arange(len(models))
    width = 0.25

    plt.figure()

    for i, temp in enumerate(temperatures):
        values = [f1_scores[temp].get(m, 0) for m in models]

        colors = []
        for m in models:
            base = MODEL_COLORS.get(m, (0.5, 0.5, 0.5))
            if temp == "0.5":
                colors.append(darken(base))
            elif temp == "1.5":
                colors.append(lighten(base))
            else:
                colors.append(base)

        plt.bar(
            x + i * width,
            values,
            width,
            label=f"Temperature {temp}",
            color=colors
        )

    plt.xticks(x + width, models, rotation=0)
    plt.ylabel("F1 score")
    plt.xlabel("Model")
    plt.title("Effect of temperature on F1 score (zero-shot)")
    plt.legend()
    plt.tight_layout()


if __name__ == "__main__":
    print("Generating strategy charts...")
    generate_strategy_chart()
    plt.show(block=False)

    print("Generating temperature charts...")
    generate_temperature_chart()
    plt.show(block=True)

    print("\nFinished!")