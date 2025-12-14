# vulnerabilities-detection

## Overview

### Results with CWE field check

| Model | f1 | precision | recall | wrong_format_responses | total_tokens | total_cost | average_cost_per_sample |
|------|------|------|------|------|------|------|------|
| zero_shot/gpt-5.1 | 0.652 | 0.724 | 0.593 | 0 | 159915 | 0.898 | 0.0036 |
| zero_shot/grok-code-fast-1 | 0.627 | 0.652 | 0.604 | 2 | 456835 | 0.507 | 0.0020 |
| zero_shot/claude-sonnet-4.5 | 0.592 | 0.603 | 0.582 | 11 | 102729 | 0.383 | 0.0015 |
| zero_shot/devstral-2512 | 0.404 | 0.451 | 0.367 | 0 | 89277 | 0.016 | 0.0001 |
| role_based/gpt-5.1 | 0.642 | 0.657 | 0.627 | 0 | 168715 | 0.962 | 0.0038 |
| role_based/grok-code-fast-1 | 0.605 | 0.601 | 0.610 | 12 | 439345 | 0.478 | 0.0019 |
| role_based/claude-sonnet-4.5 | 0.575 | 0.564 | 0.587 | 0 | 110170 | 0.409 | 0.0016 |
| role_based/devstral-2512 | 0.396 | 0.418 | 0.376 | 1 | 92162 | 0.017 | 0.0001 |
| chain_of_thought/grok-code-fast-1 | 0.609 | 0.629 | 0.591 | 3 | 453224 | 0.498 | 0.0020 |
| chain_of_thought/devstral-2512 | 0.418 | 0.463 | 0.380 | 0 | 92985 | 0.017 | 0.0001 |
| legacy/role_based/gpt-5.1 | 0.612 | 0.631 | 0.593 | 0 | 176084 | 1.020 | 0.0041 |
| legacy/role_based/grok-code-fast-1 | 0.566 | 0.587 | 0.547 | 11 | 502636 | 0.569 | 0.0023 |
| legacy/role_based/claude-sonnet-4.5 | 0.567 | 0.551 | 0.584 | 1 | 111695 | 0.413 | 0.0017 |

### Results without CWE field check (binary classification only)

| Model | f1 | precision | recall | wrong_format_responses | total_tokens | total_cost | average_cost_per_sample |
|------|------|------|------|------|------|------|------|
| zero_shot/gpt-5.1 | 0.824 | 0.791 | 0.860 | 0 | 159915 | 0.898 | 0.0036 |
| zero_shot/grok-code-fast-1 | 0.799 | 0.732 | 0.879 | 2 | 456835 | 0.507 | 0.0020 |
| zero_shot/claude-sonnet-4.5 | 0.805 | 0.708 | 0.932 | 11 | 102729 | 0.383 | 0.0015 |
| zero_shot/devstral-2512 | 0.764 | 0.667 | 0.893 | 0 | 89277 | 0.016 | 0.0001 |
| role_based/gpt-5.1 | 0.815 | 0.737 | 0.913 | 0 | 168715 | 0.962 | 0.0038 |
| role_based/grok-code-fast-1 | 0.825 | 0.709 | 0.986 | 12 | 439345 | 0.478 | 0.0019 |
| role_based/claude-sonnet-4.5 | 0.809 | 0.685 | 0.987 | 0 | 110170 | 0.409 | 0.0016 |
| role_based/devstral-2512 | 0.766 | 0.644 | 0.946 | 1 | 92162 | 0.017 | 0.0001 |
| chain_of_thought/grok-code-fast-1 | 0.804 | 0.722 | 0.906 | 3 | 453224 | 0.498 | 0.0020 |
| chain_of_thought/devstral-2512 | 0.762 | 0.668 | 0.887 | 0 | 92985 | 0.017 | 0.0001 |
| legacy/role_based/gpt-5.1 | 0.822 | 0.731 | 0.940 | 0 | 176084 | 1.020 | 0.0041 |
| legacy/role_based/grok-code-fast-1 | 0.815 | 0.712 | 0.953 | 11 | 502636 | 0.569 | 0.0023 |
| legacy/role_based/claude-sonnet-4.5 | 0.801 | 0.674 | 0.987 | 1 | 111695 | 0.413 | 0.0017 |

## All statistics

### Zero shot prompting

#### Results for gpt-5.1 (with CWE check)

```text
TP: 89
TN: 66
FP: 34
FN: 61
precision: 0.7235772357723578
recall: 0.5933333333333334
f1: 0.6520146520146521
total: 250
correct_format_responses: 250
wrong_format_responses: 0
total_prompt_tokens: 80129
total_completion_tokens: 79786
total_tokens: 159915
total_cost: 0.8980212500000001
average_cost_per_sample: 0.0035920850000000005
```

#### Results for gpt-5.1 (without CWE check)

```text
TP: 129
TN: 66
FP: 34
FN: 21
precision: 0.7914110429447853
recall: 0.86
f1: 0.8242811501597443
total: 250
correct_format_responses: 250
wrong_format_responses: 0
total_prompt_tokens: 80129
total_completion_tokens: 79786
total_tokens: 159915
total_cost: 0.8980212500000001
average_cost_per_sample: 0.0035920850000000005
```



#### Results for grok-code-fast-1 (with CWE check)

```text
TP: 90
TN: 51
FP: 48
FN: 59
precision: 0.6521739130434783
recall: 0.6040268456375839
f1: 0.6271777003484321
total: 250
correct_format_responses: 248
wrong_format_responses: 2
total_prompt_tokens: 129007
total_completion_tokens: 327828
total_tokens: 456835
total_cost: 0.5071177999999998
average_cost_per_sample: 0.002028471199999999
```

#### Results for grok-code-fast-1 (without CWE check)

```text
TP: 131
TN: 51
FP: 48
FN: 18
precision: 0.7318435754189944
recall: 0.8791946308724832
f1: 0.7987804878048781
total: 250
correct_format_responses: 248
wrong_format_responses: 2
total_prompt_tokens: 129007
total_completion_tokens: 327828
total_tokens: 456835
total_cost: 0.5071177999999998
average_cost_per_sample: 0.002028471199999999
```



#### Results for claude-sonnet-4.5 (with CWE check)

```text
TP: 85
TN: 37
FP: 56
FN: 61
precision: 0.6028368794326241
recall: 0.5821917808219178
f1: 0.5923344947735192
total: 250
correct_format_responses: 239
wrong_format_responses: 11
total_prompt_tokens: 96520
total_completion_tokens: 6209
total_tokens: 102729
total_cost: 0.382695
average_cost_per_sample: 0.00153078
```

#### Results for claude-sonnet-4.5 (without CWE check)

```text
TP: 136
TN: 37
FP: 56
FN: 10
precision: 0.7083333333333334
recall: 0.9315068493150684
f1: 0.804733727810651
total: 250
correct_format_responses: 239
wrong_format_responses: 11
total_prompt_tokens: 96520
total_completion_tokens: 6209
total_tokens: 102729
total_cost: 0.382695
average_cost_per_sample: 0.00153078
```



### Role based prompting

#### Results for gpt-5.1 (with CWE check)

```text
TP: 89
TN: 48
FP: 52
FN: 61
precision: 0.6312056737588653
recall: 0.5933333333333334
f1: 0.6116838487972509
total: 250
correct_format_responses: 250
wrong_format_responses: 0
total_prompt_tokens: 84629
total_completion_tokens: 91455
total_tokens: 176084
total_cost: 1.0203362500000006
average_cost_per_sample: 0.004081345000000003
```

#### Results for gpt-5.1 (without CWE check)

```text
TP: 141
TN: 48
FP: 52
FN: 9
precision: 0.7305699481865285
recall: 0.94
f1: 0.8221574344023325
total: 250
correct_format_responses: 250
wrong_format_responses: 0
total_prompt_tokens: 84629
total_completion_tokens: 91455
total_tokens: 176084
total_cost: 1.0203362500000006
average_cost_per_sample: 0.004081345000000003
```



#### Results for grok-code-fast-1 (with CWE check)

```text
TP: 81
TN: 34
FP: 57
FN: 67
precision: 0.5869565217391305
recall: 0.5472972972972973
f1: 0.5664335664335665
total: 250
correct_format_responses: 239
wrong_format_responses: 11
total_prompt_tokens: 133127
total_completion_tokens: 369509
total_tokens: 502636
total_cost: 0.5693228199999998
average_cost_per_sample: 0.002277291279999999
```

#### Results for grok-code-fast-1 (without CWE check)

```text
TP: 141
TN: 34
FP: 57
FN: 7
precision: 0.7121212121212122
recall: 0.9527027027027027
f1: 0.815028901734104
total: 250
correct_format_responses: 239
wrong_format_responses: 11
total_prompt_tokens: 133127
total_completion_tokens: 369509
total_tokens: 502636
total_cost: 0.5693228199999998
average_cost_per_sample: 0.002277291279999999
```



#### Results for claude-sonnet-4.5 (with CWE check)

```text
TP: 87
TN: 29
FP: 71
FN: 62
precision: 0.5506329113924051
recall: 0.5838926174496645
f1: 0.5667752442996743
total: 250
correct_format_responses: 249
wrong_format_responses: 1
total_prompt_tokens: 105218
total_completion_tokens: 6477
total_tokens: 111695
total_cost: 0.4128089999999999
average_cost_per_sample: 0.0016512359999999997
```

#### Results for claude-sonnet-4.5 (without CWE check)

```text
TP: 147
TN: 29
FP: 71
FN: 2
precision: 0.6743119266055045
recall: 0.9865771812080537
f1: 0.8010899182561307
total: 250
correct_format_responses: 249
wrong_format_responses: 1
total_prompt_tokens: 105218
total_completion_tokens: 6477
total_tokens: 111695
total_cost: 0.4128089999999999
average_cost_per_sample: 0.0016512359999999997
```


### Wrong response formats

- zero-shot, gpt-5.1: `0`
- zero-shot, grok-code-fast-1: `2` (without CWE field)
- zero-shot, claude-sonnet-4.5: `11` (blank responses)
- role-based, gpt-5.1: `0`
- role-based, grok-code-fast-1: `11` (`10` without CWE field, `1` blank responses)
- role-based, claude-sonnet-4.5: `1` (blank responses)

## Sample prompts

### Zero-shot prompting

```text
Examine the following code snippet and determine whether it contains a security vulnerability.
Return ONLY a JSON object in the following format, and nothing else:
{
  "vulnerable": true or false,
  "cwe": CODE_NUMBER
}

Code snippet:
#include <stdio.h>

#define GET_FLOAT_BITS_AS_INT(i) i

void printNum(int num) {
    printf("%d\n", num);
}

int main() {
    int a = 55;
    float b = 1.8f;

    printNum(GET_FLOAT_BITS_AS_INT(a));
    printNum(GET_FLOAT_BITS_AS_INT(b));

    return 0;
}
```

### Role-based prompting

```text
You are a senior security specialist with 20 years of experience in detecting and analyzing vulnerabilities in C/C++ applications. Review the following code snippet to identify potential vulnerabilities.
Return ONLY a JSON object in the following format, and nothing else:
{
  "vulnerable": true or false,
  "cwe": CODE_NUMBER
}

Code snippet:
#include <stdio.h>

#define GET_FLOAT_BITS_AS_INT(i) i

void printNum(int num) {
    printf("%d\n", num);
}

int main() {
    int a = 55;
    float b = 1.8f;

    printNum(GET_FLOAT_BITS_AS_INT(a));
    printNum(GET_FLOAT_BITS_AS_INT(b));

    return 0;
}
```

### Chain-of-thought prompting

```text
Examine the following code snippet and determine whether it contains a security vulnerability. Think step by step internally. Do not include your reasoning in the output.
Return ONLY a JSON object in the following format, and nothing else:
{
  "vulnerable": true or false,
  "cwe": CODE_NUMBER
}

Code snippet:
#include <stdio.h>

#define GET_FLOAT_BITS_AS_INT(i) i

void printNum(int num) {
    printf("%d\n", num);
}

int main() {
    int a = 55;
    float b = 1.8f;

    printNum(GET_FLOAT_BITS_AS_INT(a));
    printNum(GET_FLOAT_BITS_AS_INT(b));

    return 0;
}
```

## TODO

- chain-of-thought i zero-shot
- tańszy model
- temperatura
- ~~analiza bez cwe~~
- ~~artykuł: rozdział o użytych technologiach~~
