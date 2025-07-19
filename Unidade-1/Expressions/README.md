## 🐍 Unit 4 – Expressions in Python
An **expression** combines values, variables, and operators to produce a single result. In practice, nearly every non-trivial line of Python you write is an expression—or contains one.
---
### 🎯 Style & Best Practices
* **Parentheses first** – use them liberally to show precedence, even when Python would get it right without them.
* **One idea per line** – if an expression grows too long, split it and assign intermediate results to descriptively named variables.
* **Descriptive names** – a well-chosen variable name makes an expression self-explanatory.
```python
# 👍 Clear
net_price = (gross_price - discount) * (1 + tax_rate)
# 👎 Hard to read
np = gp - d * (1 + t)
```
---
### ⏫ Operator Precedence (recap)
`()` **>** `**` **>** `* / // %` **>** `+  -` **>** comparisons **>** `not` **>** `and` **>** `or`
Python follows the standard mathematical hierarchy; anything inside parentheses runs first.
---
### ✅ Arithmetic Expression Example
```python
result = 2 + 3 * 4    # 14, because * binds tighter than +
print(result)
```
---
### ✅ Boolean Expression Example
```python
is_valid = 10 > 5 and 3 < 2
print(is_valid)        # False
```
Logical operators (`and`, `or`, `not`) can chain comparisons to build complex conditions.
---
### ❌ Common Error
```python
value = 5 +           # SyntaxError → expression is incomplete
```
Always ensure both operands and the operator are present.
---
### 🚩 Tips & Edge Cases
* Division always produces `float`; use `//` if you need an `int`.
* String comparisons are lexicographic (`'apple' < 'banana'` → `True`).
* Mixing numeric types promotes to the most “complex” type: `int → float → complex`.
* An expression can be passed directly to functions: `print((2 + 3) * 4)`.
---
🎉 **Good job!** You now understand how to build and evaluate arithmetic and boolean expressions, and how operator precedence affects the final result. Next up: flow control with `if` statements.
