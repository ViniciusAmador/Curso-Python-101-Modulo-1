### 🏋️‍♂️ Exercise 1 – *Inspect & Convert Types in the Terminal*
> **Goal:** See how Python infers types and how explicit conversion changes them.
1. Open your terminal and create ``.
2. Ask the user for **any** input and store it in `data`.
3. Print the value **and** its current type with `type()`.
4. If `data.isdigit()` returns `True`, convert it to `int`.\
   Otherwise, try converting to `float` with `float()` inside a `try/except` block.\
   If conversion fails, keep it as `str`.
5. Print the new value and type so the change is visible.
```python
data = input("Enter something: ")
print("Original:", data, type(data))

if data.isdigit():
    data = int(data)
else:
    try:
        data = float(data)
    except ValueError:
        pass  # remains a string

print("After processing:", data, type(data))
```
Run the script with inputs like `42`, `3.14`, and `hello` to observe how the type adapts.
