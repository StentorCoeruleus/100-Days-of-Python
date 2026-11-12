# Tip Calculator: Python Bill Splitter

## Overview

The *Tip Calculator* is a text-based Python program I built as the final project for Day 2 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

It solves a common real-world problem: how much should each person pay when a group splits a restaurant bill and adds a tip? The user enters the total bill, chooses a tip percentage and says how many people are sharing the cost. The program then calculates each person's share, rounded to two decimal places.

The program runs entirely in the terminal, and the user interacts with it by typing their answers to its questions. This project showcases how Python can take text typed in by a user, convert it into numbers, and use arithmetic to produce a useful result.

---

## How to Play

There are three ways to try the Tip Calculator.

### Option 1: Play in your browser (no installation)

**[Launch the Tip Calculator](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%202/Tip%20Calculator%20Project/)**

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
   cd "100-Days-of-Python/Day 2/Tip Calculator Project"
   ```
3. Run the Python script:
   ```bash
   python task.py
   ```
   On macOS or Linux, you may need to type `python3 task.py` instead.
4. Follow the on-screen prompts to calculate each person's share.

### Option 3: Run it in an online Python editor

If you don't want to install anything, open `task.py` on GitHub, copy the code, and paste it into a free online Python editor such as [Programiz](https://www.programiz.com/python-programming/online-compiler/) or [Online-Python](https://www.online-python.com/). Then click **Run**.

---

## How the Program Works

The program follows a simple **input → process → output** structure. It collects three pieces of information from the user, carries out a series of calculations, and displays the result.

### 1. Welcoming the User

When the program starts, it greets the user with a welcome message so they know what the program does.

### 2. Collecting the Bill Details

The program asks the user three questions:

- How much is the total bill?
- What percentage tip would they like to give: 10, 12 or 15?
- How many people are splitting the bill?

Each answer is collected with Python's `input()` function and stored in a variable.

### 3. Calculating Each Person's Share

The program converts the tip percentage into a multiplier. For example, a 12% tip becomes `1.12`. It multiplies the bill by this multiplier to get the total including tip, then divides the total by the number of people.

### 4. Displaying the Result

The final amount is rounded to two decimal places, which matches pounds and pence, and displayed to the user.

### Example

```
Welcome to the Tip Calculator!
How much would you like to pay? £68
How much tip would you like to give? 10, 12 or 15? 12
How many people are there to split the bill? 3
Each person should pay £25.39.
```

---

## Program Flow

1. **Start:** the program displays a welcome message.
2. **Bill input:** the user enters the total cost of the bill.
3. **Tip input:** the user chooses a tip percentage.
4. **Group input:** the user enters the number of people splitting the bill.
5. **Calculation:** the program adds the tip to the bill and divides the total between the group.
6. **Outcome:** the program displays how much each person should pay.

Unlike my Day 3 Treasure Island game, this program has no branching paths. Every user follows the same sequence of steps. What changes is the **data** the user enters, which leads to a different result each time.

---

## Python Concepts Used

This project introduces several fundamental Python concepts, focusing on data types, type conversion and mathematical operations.

### 1. `print()`: Displaying Information

The `print()` function displays text in the terminal. It is used to welcome the user and to show the final result.

```python
print("Welcome to the Tip Calculator!")
```

### 2. `input()` and Variables: Collecting User Data

The `input()` function pauses the program and waits for the user to type a response. The response is stored in a variable so the program can use it later.

```python
cost = float(input("How much would you like to pay? £"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people are there to split the bill? "))
```

Each variable has a descriptive name (`cost`, `tip`, `number_of_people`), which makes the code easier to read and understand.

### 3. Data Types and Type Conversion

The `input()` function always returns a **string** (text), even when the user types a number. You can't do arithmetic with a string, so the input has to be converted into a number first:

- **`float()`** converts the input into a decimal number. I used it for the bill, because money often includes pence (e.g. `£47.50`).
- **`int()`** converts the input into a whole number. I used it for the tip percentage and the number of people, because these will always be whole numbers.

```python
cost = float(input("How much would you like to pay? £"))   # e.g. "47.50" → 47.5
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))   # e.g. "12" → 12
```

Choosing the right data type for each value is the core lesson of Day 2. Without the conversion, Python would raise a `TypeError` when it tried to multiply text by a number.

### 4. Arithmetic Operators

The program uses Python's arithmetic operators to carry out the calculation:

| Operator | Meaning | Used for |
|----------|---------|----------|
| `/` | Division | Turning the tip into a decimal (`12 / 100 = 0.12`) |
| `+` | Addition | Adding 1 to create the multiplier (`0.12 + 1 = 1.12`) |
| `*` | Multiplication | Applying the multiplier to the bill |
| `/` | Division | Splitting the total between the group |

```python
percentage = tip / 100          # 12 → 0.12
percentage += 1                 # 0.12 → 1.12
calculation_1 = cost * percentage
```

Multiplying the bill by `1.12` adds the bill and the 12% tip in a single step. This gives the same answer as `cost + (cost * 0.12)`, but it's shorter.

### 5. Assignment Operators

Assignment operators update the value of a variable using its current value:

- `+=` adds a value to the variable
- `/=` divides the variable by a value

```python
percentage += 1                          # same as: percentage = percentage + 1
calculation_1 /= int(number_of_people)   # same as: calculation_1 = calculation_1 / number_of_people
```

These shortcuts make the code more concise without changing what it does.

### 6. Rounding with `round()`

Splitting a bill often produces an answer with many decimal places. Computers also store decimal numbers in binary, which can add tiny inaccuracies. Without rounding, the example above would give:

```
25.38666666666667
```

The `round()` function fixes this by rounding the result to a set number of decimal places:

```python
calculation_2 = round(calculation_1, 2)   # 25.38666666666667 → 25.39
```

Rounding to two decimal places matches how money is written in pounds and pence.

### 7. f-Strings: Formatting the Output

An f-string lets you insert variables directly into a string by placing them inside curly brackets `{}`, with an `f` before the opening quotation mark.

```python
print(f"Each person should pay £{calculation_2}.")
```

This is cleaner than joining strings with `+`. It also converts the number to text automatically, so you don't need to call `str()` first.

---

## What I Learned

This project helped me build a solid understanding of how Python handles different kinds of data.

Key learning outcomes include:

- Using `input()` to collect information from the user and storing it in variables.
- Understanding the difference between strings, integers and floats.
- Converting between data types with `int()` and `float()`.
- Using arithmetic operators (`+`, `/`, `*`) to perform calculations.
- Using assignment operators (`+=`, `/=`) to update variables concisely.
- Turning a percentage into a multiplier to simplify a calculation.
- Understanding why floating-point numbers can produce small inaccuracies, and using `round()` to fix them.
- Formatting output clearly with f-strings.
- Breaking a real-world problem down into clear, logical steps.

The most important lesson was that data types matter. The same characters, such as `"12"` and `12`, behave completely differently depending on whether Python treats them as text or as a number. Converting user input into the correct type is essential before any calculation can take place.

---

## Future Improvements

Possible extensions to the project include:

- Always show two decimal places: `round()` removes any extra decimal places, but it doesn't add a missing zero at the end. For example, a £150 bill with a 12% tip split between 5 people displays *£33.6* instead of *£33.60*:

  ```
  Welcome to the Tip Calculator!
  How much would you like to pay? £150
  How much tip would you like to give? 10, 12 or 15? 12
  How many people are there to split the bill? 5
  Each person should pay £33.6.
  ```

  This could be fixed with an f-string format specifier, `f"{calculation_1:.2f}"`, which always displays exactly two decimal places.
- **Input validation:** ask the user to try again if they enter something that isn't a number, instead of the program crashing.
- **Restrict or customise the tip:** check that the tip is 10, 12 or 15, or let the user enter any percentage they like.
- **Prevent division by zero:** make sure the number of people is at least 1.
- **Uneven splits:** allow people to pay different amounts, for example if someone ordered more.
- **Functions:** move the calculation into a reusable function to improve organisation.

These improvements would build on the existing program and give me the chance to practise more advanced Python concepts, such as loops, error handling and functions.

---

## Files

| File | Description |
|------|-------------|
| [`task.py`](task.py) | The Tip Calculator program |
| `index.html` | Runs the program in a web browser using Pyodide |

---

## Course Context

This project was completed as part of Day 2 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 2 focuses on data types, type conversion, mathematical operations and f-strings. The Tip Calculator puts all of these into practice to solve an everyday problem. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.