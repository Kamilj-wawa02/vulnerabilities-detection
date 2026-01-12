import matplotlib.pyplot as plt

# Dane: wszystkie instancje, sumowanie per model
data = [
    # model, wrong_format_responses
    ("gpt-5.1", [0,0,0,0]),                 # zero-shot, temperatures, chain_of_thought, legacy
    ("grok-code-fast-1", [2,12,3,5,11]),    # zero-shot, role-based, chain_of_thought, temperatures, legacy
    ("claude-sonnet-4.5", [11,0,17,1]),     # zero-shot, role-based, chain_of_thought, legacy
    ("devstral-2512", [0,1,0,0,15])         # zero-shot, role-based, chain_of_thought, temperatures x2
]

# Sumowanie wrong format responses
models = []
wrong_format_totals = []
for model, counts in data:
    models.append(model)
    wrong_format_totals.append(sum(counts))

# Kolory przyjazne dla osób z daltonizmem (Paul Tol)
colors = ["#4477AA", "#EE6677", "#228833", "#CCBB44"]  # niebieski, czerwony, zielony, żółty

plt.figure(figsize=(9,6))
bars = plt.bar(models, wrong_format_totals, color=colors, edgecolor="black")

# Dodanie wartości nad słupkami
for bar, value in zip(bars, wrong_format_totals):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.5,
        str(value),
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.ylabel("Total wrong format responses")
plt.xlabel("Model")
plt.title("Wrong format responses per model (sum across prompt techniques)\nIncludes CWE verification")
plt.ylim(0, max(wrong_format_totals) + 5)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()



















#==================================================
# Token_Efficiency_Zero_Shot
#==================================================
# import matplotlib.pyplot as plt

# # Dane: tylko zero-shot
# models = [
#     "gpt-5.1",
#     "grok-code-fast-1",
#     "claude-sonnet-4.5",
#     "devstral-2512"
# ]

# f1_scores = [0.652, 0.627, 0.592, 0.404]
# total_tokens = [159915, 456835, 102729, 89277]

# # Color-blind friendly palette (Okabe–Ito)
# colors = ["#0072B2", "#E69F00", "#009E73", "#D55E00"]

# plt.figure(figsize=(9, 6))

# bars = plt.bar(models, f1_scores, color=colors, edgecolor="black")

# # Adnotacje: liczba tokenów nad słupkami
# for bar, tokens in zip(bars, total_tokens):
#     plt.text(
#         bar.get_x() + bar.get_width() / 2,
#         bar.get_height() + 0.015,
#         f"{tokens:,} tokens",
#         ha="center",
#         va="bottom",
#         fontsize=9
#     )

# plt.ylabel("F1-score")
# plt.xlabel("Model (zero-shot)")
# plt.title("Token efficiency (zero-shot)\nF1-score vs total tokens")

# plt.ylim(0, 0.75)
# plt.grid(axis="y", linestyle="--", alpha=0.6)

# plt.tight_layout()
# plt.show()











#==================================================
# Koszt_vs_skutecznosc_modeli_LLM
#==================================================
# import matplotlib.pyplot as plt

# # Dane
# data = [
#     # model, prompting, f1, cost
#     ("gpt-5.1", "zero-shot", 0.652, 0.0036),
#     ("grok-code-fast-1", "zero-shot", 0.627, 0.0020),
#     ("claude-sonnet-4.5", "zero-shot", 0.592, 0.0015),
#     ("devstral-2512", "zero-shot", 0.404, 0.0001),

#     ("gpt-5.1", "role-based", 0.642, 0.0038),
#     ("grok-code-fast-1", "role-based", 0.605, 0.0019),
#     ("claude-sonnet-4.5", "role-based", 0.575, 0.0016),
#     ("devstral-2512", "role-based", 0.396, 0.0001),

#     ("gpt-5.1", "chain-of-thought", 0.655, 0.0037),
#     ("grok-code-fast-1", "chain-of-thought", 0.609, 0.0020),
#     ("claude-sonnet-4.5", "chain-of-thought", 0.562, 0.0015),
#     ("devstral-2512", "chain-of-thought", 0.418, 0.0001),
# ]

# # Mapowanie kolorów na modele
# model_colors = {
#     "gpt-5.1": "tab:blue",
#     "grok-code-fast-1": "tab:orange",
#     "claude-sonnet-4.5": "tab:green",
#     "devstral-2512": "tab:red"
# }

# # Mapowanie markerów na techniki promptowania
# prompt_markers = {
#     "zero-shot": "o",
#     "role-based": "s",
#     "chain-of-thought": "^"
# }

# plt.figure(figsize=(10, 6))

# for model, prompting, f1, cost in data:
#     plt.scatter(
#         cost,
#         f1,
#         color=model_colors[model],
#         marker=prompt_markers[prompting],
#         s=90,
#         edgecolors="black"
#     )

# # Legendy (oddzielne)
# for model, color in model_colors.items():
#     plt.scatter([], [], color=color, label=model)

# for prompting, marker in prompt_markers.items():
#     plt.scatter([], [], color="black", marker=marker, label=prompting)

# plt.xlabel("Average cost per sample [USD]")
# plt.ylabel("F1-score")
# plt.title("Koszt vs skuteczność modeli LLM\nF1-score vs average_cost_per_sample")

# plt.grid(True, linestyle="--", alpha=0.6)
# plt.legend(title="Model / Prompting", loc="lower right")
# plt.tight_layout()
# plt.show()













#==================================================
#Porownanie_F1_Precision_Recall_w_ZeroShot
#==================================================

# import matplotlib.pyplot as plt
# import numpy as np

# # Dane: tylko zero-shot
# models = [
#     "gpt-5.1",
#     "grok-code-fast-1",
#     "claude-sonnet-4.5",
#     "devstral-2512"
# ]

# f1 = [0.652, 0.627, 0.592, 0.404]
# precision = [0.724, 0.652, 0.603, 0.451]
# recall = [0.593, 0.604, 0.582, 0.367]

# x = np.arange(len(models))
# width = 0.25

# # Stonowane kolory (colorblind-friendly)
# colors = {
#     "f1": "#DDAA33",
#     "precision": "#BB5566",
#     "recall": "#004488"
# }

# plt.figure(figsize=(10, 6))

# bars_f1 = plt.bar(x - width, f1, width, label="F1-score", color=colors["f1"])
# bars_precision = plt.bar(x, precision, width, label="Precision", color=colors["precision"])
# bars_recall = plt.bar(x + width, recall, width, label="Recall", color=colors["recall"])

# # Dodanie pełnych wartości nad słupkami (bez zaokrąglania)
# def add_labels(bars, values):
#     for bar, value in zip(bars, values):
#         plt.text(
#             bar.get_x() + bar.get_width() / 2,
#             bar.get_height() + 0.015,
#             str(value),
#             ha="center",
#             va="bottom",
#             fontsize=9
#         )

# add_labels(bars_f1, f1)
# add_labels(bars_precision, precision)
# add_labels(bars_recall, recall)

# plt.xticks(x, models, rotation=15)
# plt.ylabel("Score")
# plt.xlabel("Model (zero-shot)")
# plt.title("Porównanie jakości modeli (zero-shot)\nF1 / Precision / Recall")
# plt.ylim(0, 1.0)

# plt.legend()
# plt.grid(axis="y", linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.show()
