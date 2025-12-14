# vulnerabilities-detection

## Overview

### Results with CWE field check

These results include verification of the CWE field in the model's response to ensure it matches the expected vulnerability code.

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
| temperatures/zero_shot/0.5/grok-code-fast-1 | 0.623 | 0.634 | 0.612 | 5 | 405818 | 0.431 | 0.0017 |
| temperatures/zero_shot/0.5/gpt-5.1 | 0.639 | 0.733 | 0.567 | 0 | 166901 | 0.968 | 0.0039 |
| temperatures/zero_shot/1.5/gpt-5.1 | 0.632 | 0.724 | 0.560 | 0 | 158766 | 0.887 | 0.0035 |
| legacy/role_based/gpt-5.1 | 0.612 | 0.631 | 0.593 | 0 | 176084 | 1.020 | 0.0041 |
| legacy/role_based/grok-code-fast-1 | 0.566 | 0.587 | 0.547 | 11 | 502636 | 0.569 | 0.0023 |
| legacy/role_based/claude-sonnet-4.5 | 0.567 | 0.551 | 0.584 | 1 | 111695 | 0.413 | 0.0017 |

**Note: Legacy role-based prompting refers to the previous version of role-based prompts used before improvements were made.**

### Results without CWE field check (binary classification only)

These results do not include verification of the CWE field, focusing solely on whether the code is vulnerable or not.

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
| temperatures/zero_shot/0.5/grok-code-fast-1 | 0.798 | 0.717 | 0.898 | 5 | 405818 | 0.431 | 0.0017 |
| temperatures/zero_shot/0.5/gpt-5.1 | 0.809 | 0.799 | 0.820 | 0 | 166901 | 0.968 | 0.0039 |
| temperatures/zero_shot/1.5/gpt-5.1 | 0.814 | 0.796 | 0.833 | 0 | 158766 | 0.887 | 0.0035 |
| legacy/role_based/gpt-5.1 | 0.822 | 0.731 | 0.940 | 0 | 176084 | 1.020 | 0.0041 |
| legacy/role_based/grok-code-fast-1 | 0.815 | 0.712 | 0.953 | 11 | 502636 | 0.569 | 0.0023 |
| legacy/role_based/claude-sonnet-4.5 | 0.801 | 0.674 | 0.987 | 1 | 111695 | 0.413 | 0.0017 |

## Common issues in model responses

Models that had non-zero wrong_format_responses encountered the following issues:

- Blank responses (e.g. zero_shot/claude-sonnet-4.5, role-based/grok-code-fast-1)

- Missing CWE field in the JSON response (e.g. zero_shot/grok-code-fast-1, role-based/grok-code-fast-1).
  The model did provide the "vulnerable" field but omitted the "cwe" field. This happened when
  the code snippet was not vulnerable (the model was supposed to maintain the requested response format
  at all times, therefore such response is incorrect).

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

- ~~chain-of-thought~~ and ~~zero-shot~~
- ~~cheaper model~~
- temperature
- ~~analysis without CWE~~
- ~~article: chapter on used technologies~~