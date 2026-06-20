# Calculator Project Tutorial

Welcome! This tutorial is designed for beginner Python programmers who want to build their **first real project**: a console-level calculator that evaluates simple mathematical expressions.

## 🎯 Project Goal

Create a Python program that:
- Takes user input for mathematical expressions (e.g., `5 + 3`, `10 * 2`, `20 / 4`)
- Parses the expression to extract numbers and operators
- Performs the calculation
- Displays the result to the user
- Repeats until the user decides to quit

This project will help you practice fundamental Python concepts while building something functional and satisfying!

## 📚 Python Concepts You'll Use

### 1. **Variables and Data Types**
Store information in your program using variables and understand different data types:
```python
number = 5              # integer
price = 19.99          # float
message = "Hello"      # string
is_valid = True        # boolean
```

### 2. **String Methods**
Manipulate and analyze text using built-in string methods:
```python
user_input = "  5 + 3  "
user_input.strip()      # Remove whitespace: "5 + 3"

expression = "5 + 3 * 2"
expression.split()      # Split by spaces: ["5", "+", "3", "*", "2"]
expression.split("+")   # Split by operator: ["5 ", " 3 * 2"]

operator = "+"
operator.lower()        # Convert to lowercase (useful for validating input)
```

### 3. **Type Conversion**
Convert between different data types:
```python
num_string = "42"
num_int = int(num_string)        # Convert string to integer
num_float = float(num_string)    # Convert string to float
back_to_string = str(num_int)    # Convert back to string
```

### 4. **Input and Output**
Get user input and display results:
```python
user_input = input("Enter an expression: ")  # Get input from user
print("The result is:", result)              # Display output
```

### 5. **Conditional Statements (if, elif, else)**
Make decisions based on conditions:
```python
number = 10

if number > 5:
    print("Number is greater than 5")
elif number == 5:
    print("Number is exactly 5")
else:
    print("Number is less than 5")
```

### 6. **While Loops**
Repeat actions multiple times:
```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count = count + 1

# Keep asking user until they quit
while True:
    user_input = input("Enter something (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    print(f"You entered: {user_input}")
```

### 7. **Operators**
Perform calculations and comparisons:
```python
# Arithmetic operators
result = 10 + 5   # Addition
result = 10 - 5   # Subtraction
result = 10 * 5   # Multiplication
result = 10 / 5   # Division

# Comparison operators
if a > b:
    pass
if a == b:
    pass
if a != b:
    pass
```

### 8. **Comments and Code Organization**
Document your code and keep it readable:
```python
# This is a comment explaining the code below
variable = 42  # You can add comments on the same line too
```

## 🚀 Getting Started

1. **Open the `calculator.py` file** in your editor or IDE (VS Code, PyCharm, IDLE, etc.)
2. **Read the TODO comment** at the top of the file
3. **Start coding!** Use only the Python concepts listed above
4. **Test your program** by running it and trying different expressions
5. **Debug** if something doesn't work as expected

## 💡 Step-by-Step Hints

Here's how you might approach this:

### Step 1: Get User Input
Ask the user to enter an expression:
```python
expression = input("Enter a mathematical expression (e.g., '5 + 3'): ")
```

### Step 2: Parse the Expression
Separate the numbers and operator from the input string:
- Use `.split()` or `.strip()` to extract parts
- Identify which operator was used (+, -, *, /)

### Step 3: Convert to Numbers
Convert the string numbers to integers or floats:
```python
num1 = float(number_string)
num2 = float(another_number_string)
```

### Step 4: Perform the Calculation
Use conditional statements to determine which operation to perform:
```python
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
# ... and so on
```

### Step 5: Display the Result
Print the result to the user:
```python
print(f"{num1} {operator} {num2} = {result}")
```

### Step 6: Repeat (Optional)
Use a `while` loop to let the user calculate multiple expressions

## ⚠️ Prohibited Section

To maintain the learning value of this project, **DO NOT USE** these tools and techniques:

### ❌ Built-in Functions to Avoid
- **`eval()`** - Evaluates Python code from a string (defeats the purpose!)
  ```python
  # DON'T do this:
  result = eval("5 + 3")  # This is cheating! 😄
  ```
- **`exec()`** - Executes Python code from a string
  ```python
  # DON'T do this:
  exec("result = 5 + 3")
  ```

### ❌ External Libraries to Avoid
- **`sympy`** - Symbolic mathematics library
- **`numpy`** - Numerical computing library
- **`ast.literal_eval()`** - Abstract syntax tree parsing (still cheating!)
- **`operator` module** - Pre-built operations (defeats learning purpose)

### ⚠️ Techniques to Avoid
- Using `reduce()` or `map()` for calculation
- Importing calculation libraries
- Using regex (regular expressions) for parsing

**Why?** These tools are powerful, but using them here would skip the learning experience. The goal is to understand *how* to build a calculator yourself, not to use someone else's solution!

## 🎓 Learning Outcomes

After completing this project, you'll understand:
- ✅ How to work with strings and split them into parts
- ✅ How to convert between different data types
- ✅ How to use conditional logic to make decisions
- ✅ How to validate user input
- ✅ How to build a simple interactive program
- ✅ How to debug and test your code

## 📋 Testing Your Program

Try these test cases once you're done:
```
5 + 3         → Should output: 8
10 - 2        → Should output: 8
4 * 3         → Should output: 12
20 / 4        → Should output: 5.0
100 + 50 - 25 → Handle this or output an error message
```

## 🤝 Need Help?

If you get stuck:
1. **Re-read** the hints and Python concepts section
2. **Check** the `solutions/` directory for a working example
3. **Debug** by adding `print()` statements to see what's happening
4. **Ask** for help from fellow learners or your mentor

## 📝 Next Steps (After Completing)

Once you've completed the basic calculator:
- Add support for multiple operators in one expression (e.g., `5 + 3 * 2`)
- Add input validation to handle errors gracefully
- Add more operators like `**` (power) or `%` (modulo)
- Build a GUI version using `tkinter`
- Explore intermediate concepts like functions and classes

---

**Good luck! Remember: struggling with code is part of learning. Enjoy the process! 🎉**
