
### 🏋️‍♂️ Exercise 1 – Evaluate & Explain *(Terminal Only)*
Create **`exercise-unit4.py`** that:
1. Prompts the user for **three integers** `a`, `b`, `c`.
2. Evaluates the expression `a + b * c - (a % b)`.
3. Prints the **result** *and* a step-by-step breakdown showing operator precedence.
Example output:
```text
Enter a: 5
Enter b: 2
Enter c: 3
Expression: 5 + 2 * 3 - (5 % 2)
Step-by-step:
  1) 2 * 3  = 6
  2) 5 % 2  = 1
  3) 5 + 6  = 11
  4) 11 - 1 = 10
Result: 10
```
*Hint*: Compute sub-results in separate variables (`step1 = b * c`, etc.) before combining them.
