# Calculator: Python Command-Line Calculator

## Overview

The *Calculator* is a text-based Python program I built as the final project for Day 10 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

It works like a basic pocket calculator. It can add, subtract, multiply and divide two numbers. After each calculation, the user can carry on using the answer in the next sum, start a fresh calculation, or quit. Because of this, the user can chain several calculations together, just like pressing `=` and continuing on a real calculator.

The program runs entirely in the terminal and opens with an ASCII art calculator logo. The user interacts with it by typing numbers and operators. The project shows how functions with outputs can be stored in a dictionary and chosen while the program is running, which makes the code shorter, cleaner and easier to extend.

---

## How to Play

There are three ways to try the Calculator.

### Option 1: Play in your browser (no installation)

**[Launch the Calculator](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%2010/Calculator%20Project/)**

This runs the Python code directly in your web browser using [Pyodide](https://pyodide.org/). Click *Start*, type your answers into the box, and press *Enter*.

### Option 2: Run it on your computer with Python 3

**Requirements**

- Python 3 installed on your computer. You can download it from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"** during installation.
- A terminal, command prompt, or Python-compatible IDE (e.g. PyCharm, VS Code or IDLE)

No external libraries are required.

**Installation and Execution**

1. Download the project files in one of two ways:
   - **Download ZIP:** on the repository's main page, click the green **Code** button, then **Download ZIP**, and extract the folder.
   - **Clone the repository** using Git:
     ```bash
     git clone https://github.com/StentorCoeruleus/100-Days-of-Python.git
     ```
2. Open a terminal in the project folder:
   ```bash
   cd "100-Days-of-Python/Day 10/Calculator Project"
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```
   On macOS or Linux, you may need to type `python3 main.py` instead.
4. Follow the on-screen prompts to start calculating.

**Important:** keep `main.py` and `art.py` in the **same folder**. `main.py` imports the logo from `art.py`, so the program won't run without it.

### Option 3: Run it in an online Python editor

Because this program is split across two files, it needs an online editor that supports multiple files, such as [Replit](https://replit.com/). Create a new Python project, add `art.py` as an extra file, paste in the code for both files, and click **Run**.

---

## How the Program Works

The program follows a loop structure. It keeps asking for calculations until the user chooses to quit, and it remembers the last answer so it can be reused.

### 1. Starting the Calculator

When the program starts, it imports and displays the calculator logo from `art.py`.

### 2. Entering the First Calculation

The program asks the user for:

- a first number
- an operator, chosen from a list of `+`, `-`, `*` and `/`
- a second number

The numbers are converted to decimals with `float()`, so the calculator works with whole numbers and decimals alike.

### 3. Calculating the Answer

The program looks up the chosen operator in a dictionary to find the matching function: `add`, `subtract`, `multiply` or `divide`. It then calls that function with the two numbers and displays the full calculation, e.g. `12.0 * 3.0 = 36.0`.

### 4. Choosing What to Do Next

After each answer, the user chooses one of three options:

- **`ans`:** continue calculating, using the answer as the new first number
- **`no`:** clear the screen and start a brand-new calculation
- **`exit`:** quit the calculator

If the user types anything else, for example a typo like `anss`, the calculator doesn't quit or crash. It displays a friendly message and carries on:

- If the user was starting a fresh calculation, it begins a new calculation.
- If the user was continuing with a previous answer, it keeps using the latest answer.

### 5. Continuing with the Previous Answer

If the user types `ans`, the program saves the answer and skips asking for a first number. The user only needs to enter a new operator and a second number, so they can chain calculations together, e.g. `12 × 3 = 36`, then `36 ÷ 4 = 9`.

### Example

```
Enter your first number:
12
+
-
*
/
Enter your operator:
*
Enter your second number:
3
12.0 * 3.0 = 36.0
Type 'ans' to continue calculating with 36.0, or type 'no' to start a new calculation, or type 'exit' to quit.
ans
+
-
*
/
Enter your operator:
/
Enter your second number:
4
36.0 / 4.0 = 9.0
Type 'ans' to continue calculating with 9.0, or type 'no' to start a new calculation, or type 'exit' to quit.
anss
Sorry, that wasn't an option. Continuing with your last answer...
+
-
*
/
Enter your operator:
-
Enter your second number:
2
9.0 - 2.0 = 7.0
Type 'ans' to continue calculating with 7.0, or type 'no' to start a new calculation, or type 'exit' to quit.
exit
```

---

## Program Flow

1. **Start:** the program displays the calculator logo.
2. **First number:** the user enters a number, unless they are continuing with a previous answer.
3. **Operator:** the program lists the available operators and the user chooses one.
4. **Second number:** the user enters a second number.
5. **Calculation:** the matching function is looked up in the dictionary and called.
6. **Result:** the program displays the full calculation and answer.
7. **Next step:** the user chooses to continue with the answer (`ans`), start again (`no`) or quit (`exit`). Any other input displays a message, and the calculator carries on.
8. **Repeat or end:** the loop repeats until the user types `exit`.

Unlike my earlier projects, this program remembers information between rounds. The answer from one calculation can become the starting point of the next. Two Boolean flags control this: one for whether the program is still running, and one for whether to reuse the last answer.

---

## Modular Code

The project is split across two files:

| File | Description |
|------|-------------|
| [`main.py`](main.py) | The calculator logic: the four operation functions, the dictionary and the main loop |
| [`art.py`](art.py) | The ASCII art calculator logo |
| `index.html` | Runs the calculator in a web browser using Pyodide |

Keeping the large ASCII logo in its own file keeps `main.py` focused on the calculator's logic and easier to read.

---

## Python Concepts Used

This project introduces several important Python concepts, focusing on functions with outputs, dictionaries and program control with `while` loops**.

### 1. Functions with Outputs: `return`

A function is a named, reusable block of code. On earlier days I used functions that only did something, like printing. On Day 10 I learned to write functions that give back a result using the `return` keyword:

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

`n1` and `n2` are parameters: placeholders for the values passed into the function. When the function is called, `return` sends the result back to the line of code that called it, so it can be stored in a variable:

```python
answer = add(12, 3)   # answer is now 15
```

The difference between `print()` and `return` is a key lesson. `print()` only shows a value on screen. `return` hands the value back so the program can keep using it, such as saving the answer for the next calculation.

### 2. Dictionaries: Storing Functions

A dictionary stores data as key: value pairs inside curly brackets `{}`. In this project, each key is an operator symbol and each value is the function that performs that operation:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

The functions are written without brackets (`add`, not `add()`). This stores the function itself, ready to be called later, instead of calling it straight away.

### 3. Calling a Function from a Dictionary

Once the user has chosen an operator, the program looks up the matching function in the dictionary and calls it in a single line:

```python
answer = operations[operator](first_number, second_number)
```

Step by step, if the user chooses `*`:

1. `operations["*"]` looks up the key `"*"` and finds the `multiply` function.
2. `(first_number, second_number)` calls that function with the two numbers.
3. The result is stored in `answer`.

This replaces a long chain of `if` / `elif` statements like this:

```python
if operator == "+":
    answer = add(first_number, second_number)
elif operator == "-":
    answer = subtract(first_number, second_number)
# ...and so on
```

To add a new operation, such as powers (`**`), I would only need to write one new function and add one line to the dictionary.

### 4. Looping Through a Dictionary

A `for` loop can go through a dictionary's keys. The program uses this to show the user which operators are available:

```python
for key in operations:
    print(key)
```

Because the list comes straight from the dictionary, it updates automatically if a new operation is added.

### 5. `while` Loops and Boolean Flags

The program uses a `while` loop to keep running until the user chooses to quit. Two **Boolean flags** (variables that are either `True` or `False`) control what happens:

```python
game_running = True
same_calculation = False

while game_running:
    if not same_calculation:
        # ask for a first number
    elif same_calculation:
        # reuse the previous answer
```

- `game_running` keeps the loop going. Setting it to `False` ends the program.
- `same_calculation` decides whether the next round asks for a new first number or reuses the last answer.

### 6. Saving the Previous Answer

When the user types `ans`, the answer is stored in a variable and becomes the first number of the next calculation:

```python
elif continue_calculation == "ans":
    saved_answer = answer
    same_calculation = True
```

```python
first_number = float(saved_answer)
```

This is what lets the user chain calculations together.

### 7. `if`, `elif` and `else`: Handling Every Possible Input

After each calculation, an `if` / `elif` / `else` statement decides what happens next:

```python
if continue_calculation == "no":
    print("\n" * 100)
    same_calculation = False

elif continue_calculation == "ans":
    saved_answer = answer
    same_calculation = True

elif continue_calculation == "exit":
    game_running = False

else:
    print("Sorry, that wasn't an option. Starting a new calculation...")
```

Each `if` and `elif` checks for one valid option. The `else` at the end catches everything else, such as typos, so the program always has a sensible response, whatever the user types.

### 8. Truthiness: A Bug I Found and Fixed

My first version of the program checked for `exit` like this:

```python
elif "exit":
    game_running = False
```

This looks correct, but it contains a bug. It doesn't compare the user's input to anything. It only checks whether the string `"exit"` is "truthy". In Python, any non-empty string counts as `True`, so this condition was always true. As a result, any answer other than `ans` or `no`, even a simple typo, would quit the calculator.

I fixed it by comparing the user's input to `"exit"` with the `==` operator:

```python
elif continue_calculation == "exit":
    game_running = False
```

I then added an `else` statement to catch any invalid input and display a helpful message instead of quitting. This taught me the importance of testing edge cases. The program had worked perfectly when I typed the expected answers, and the bug only appeared when I tested unexpected input.

### 9. `float()`: Working with Decimals

The user's input is converted with `float()` rather than `int()`, so the calculator can handle decimals as well as whole numbers:

```python
first_number = float(input("Enter your first number:\n"))
```

This is why results are shown with a decimal point, e.g. `36.0`.

### 10. `.lower()`: Handling Uppercase Input

The user's choice is converted to lowercase, so `ANS`, `Ans` and `ans` all work the same way:

```python
continue_calculation = input("Type 'ans' to continue... ").lower()
```

### 11. String Multiplication: Clearing the Screen

When the user starts a new calculation, the program "clears" the screen by printing 100 blank lines:

```python
print("\n" * 100)
```

Multiplying a string by a number repeats it, so `"\n" * 100` creates 100 new lines. This pushes the old calculations out of view.

### 12. Importing a Module: The Logo

The ASCII art logo is stored in `art.py` and imported at the start of the program:

```python
import art

print(art.logo)
```

The logo is written as a raw string (`r"""..."""`), so its backslashes are displayed exactly as typed instead of being treated as escape sequences.

---

## What I Learned

This project helped me understand how functions can be used as building blocks to make programs shorter, more organised and easier to extend.

Key learning outcomes include:

- Writing functions that return a value, using parameters.
- Understanding the difference between `print()` and `return`.
- Creating dictionaries with key: value pairs.
- Storing functions as values in a dictionary and calling them by key.
- Replacing long `if` / `elif` chains with a dictionary lookup.
- Looping through a dictionary's keys.
- Using a `while` loop with Boolean flags to control a program.
- Saving a value so it can be reused in later rounds.
- Using `else` to handle invalid input gracefully.
- Understanding truthiness: why `elif "exit":` is always `True`, and fixing it with a proper comparison (`==`).
- Debugging by testing unexpected input, not just the expected answers.
- Converting input to decimals with `float()`.
- Using `.lower()` to make user input consistent.
- Repeating a string with the `*` operator.
- Importing ASCII art from a separate module.

The most important lesson was that functions are values. Just like numbers or strings, functions can be stored in variables and dictionaries and passed around a program. Choosing which function to run based on the user's input made the calculator much cleaner than writing a separate `if` statement for every operation.

---

## Future Improvements

Possible extensions to the project include:

- **Prevent division by zero:** dividing by `0` currently crashes the program with a `ZeroDivisionError`. The program could check for this and ask for a different number.
- **Validate the operator:** an operator that isn't in the dictionary causes a `KeyError`. The program could ask the user to try again instead.
- **Validate numbers:** ask again if the user types something that isn't a number, instead of crashing.
- **Remove repeated code:** the two branches of the loop contain almost the same code. They could be combined into one reusable function, using a parameter or **recursion** to decide whether to reuse the previous answer.
- **More operations:** add powers (`**`), square roots or percentages. Thanks to the dictionary, each one would only need a new function and one new line.
- **Calculation history:** keep a list of past calculations and show them on request.
- **Neater output:** show whole numbers without `.0` (e.g. `36` instead of `36.0`).
- **Docstrings:** add a short description to each function explaining what it does.

These improvements would build on the existing program and give me the chance to practise more advanced Python concepts, such as error handling, recursion and docstrings.

---

## Course Context

This project was completed as part of Day 10 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 10 focuses on functions with outputs: using `return`, understanding the difference between printing and returning a value, and writing docstrings. The Calculator brings these together with dictionaries (Day 9) and `while` loops to build a flexible, reusable program. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.