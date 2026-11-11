# PyPassword Generator: Python Random Password Creator

## Overview

The **PyPassword Generator** is a text-based Python program I built as the final project for **Day 5** of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

It tackles an everyday security problem: creating strong, unpredictable passwords. Weak or reused passwords are one of the most common ways that online accounts are compromised. A password made from a random selection of letters, numbers and symbols is much harder to guess or crack.

The user chooses how many letters, symbols and numbers they want in their password. The program picks random characters from each group, shuffles them into a random order, and displays the finished password.

The program runs entirely in the terminal, and the user interacts with it by typing their answers to its questions. This project showcases how **loops** and Python's **`random` module** can automate a repetitive task and produce a different result every time the program runs.

---

## How to Play

There are three ways to try the PyPassword Generator.

### Option 1: Play in your browser (no installation)

**[Launch the PyPassword Generator](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%205/Password%20Generator%20Project/)**

This runs the Python code directly in your web browser using [Pyodide](https://pyodide.org/). Click **Start** and follow the prompts.

### Option 2: Run it on your computer with Python 3

**Requirements**

- Python 3 installed on your computer. You can download it from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"** during installation.
- A terminal, command prompt, or Python-compatible IDE (e.g. PyCharm, VS Code or IDLE)

No external libraries are required. The `random` module comes built into Python.

**Installation and Execution**

1. Download the project files in one of two ways:
   - **Download ZIP:** on the repository's main page, click the green **Code** button, then **Download ZIP**, and extract the folder.
   - **Clone the repository** using Git:
     ```bash
     git clone https://github.com/StentorCoeruleus/100-Days-of-Python.git
     ```
2. Open a terminal in the project folder:
   ```bash
   cd "100-Days-of-Python/Day 5/Password Generator Project"
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```
   On macOS or Linux, you may need to type `python3 main.py` instead.
4. Follow the on-screen prompts to generate your password.

### Option 3: Run it in an online Python editor

If you don't want to install anything, open `main.py` on GitHub, copy the code, and paste it into a free online Python editor such as [Programiz](https://www.programiz.com/python-programming/online-compiler/) or [Online-Python](https://www.online-python.com/). Then click **Run**.

---

## How the Program Works

The program follows an **input → process → output** structure. It collects the user's requirements, builds the password using loops and random selection, and displays the result.

### 1. Setting Up the Character Lists

At the top of the program, three lists store every character the password could contain:

- **Letters:** all 26 letters of the alphabet, in both lowercase and uppercase (52 characters in total)
- **Numbers:** the digits `0` to `9`
- **Symbols:** `! # $ % & ( ) * +`

### 2. Collecting the User's Requirements

The program welcomes the user and asks three questions:

- How many letters would you like in your password?
- How many symbols would you like?
- How many numbers would you like?

Each answer is converted into a whole number with `int()` and stored in a variable.

### 3. Picking Random Characters

The program uses a separate `for` loop for each character type. Each loop runs as many times as the user asked for. On every pass, it picks a random character from the right list and adds it to a combined list.

### 4. Shuffling the Characters

At this point, the combined list is grouped by type: all the letters, then all the numbers, then all the symbols. A pattern like that is easier to guess. The program **shuffles** the list into a random order to remove the pattern.

### 5. Building and Displaying the Password

Finally, a loop joins every character in the shuffled list into a single string, and the program displays the finished password.

### Example

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
6
How many symbols would you like?
2
How many numbers would you like?
3
Your PyPassword is k7#Rq2mT$a9
```

*Because the program picks characters at random, it creates a different password every time it runs, even with the same inputs.*

---

## Program Flow

1. **Start:** the program displays a welcome message.
2. **Letters input:** the user chooses how many letters to include.
3. **Symbols input:** the user chooses how many symbols to include.
4. **Numbers input:** the user chooses how many numbers to include.
5. **Random selection:** three `for` loops pick random characters and add them to a combined list.
6. **Shuffle:** the combined list is shuffled into a random order.
7. **Build:** the characters are joined into a single password string.
8. **Outcome:** the program displays the generated password.

The course offers two difficulty levels for this project:

- **Easy:** the characters stay in order (letters, then numbers, then symbols), e.g. `abcdef12!#`.
- **Hard:** the characters are shuffled into a random order, e.g. `k7#Rq2mT$a9`.

**I completed the hard version.**

---

## Python Concepts Used

This project introduces several fundamental Python concepts, focusing on **loops**, **lists** and **randomisation**.

### 1. Importing Modules: `import random`

A **module** is a file of ready-made Python code that you can bring into your own program. Python's built-in `random` module provides functions for generating random choices.

```python
import random
```

Importing a module at the top of the program makes all its functions available through the `random.` prefix. That way, I didn't have to write my own randomisation code.

### 2. Lists: Storing Collections of Data

A **list** stores several values in a single variable, inside square brackets `[]` and separated by commas. Each character type has its own list:

```python
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
```

The numbers are stored as **strings** (`'0'`) rather than integers (`0`). That's because they'll be joined together with letters and symbols as text, not used in calculations.

I also created an **empty list** to collect the characters chosen for the password:

```python
combined_list = []
```

### 3. `for` Loops and `range()`: Repeating an Action

A `for` loop repeats a block of code a set number of times. The `range()` function creates a sequence of numbers for the loop to step through.

```python
for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    combined_list.append(random_letter)
```

If the user asks for 6 letters, `range(0, 6)` produces the numbers 0 to 5. The loop therefore runs **6 times** and picks one random letter on each pass.

Note that `range()` stops **before** its end number. That's why `range(0, 6)` gives six values, not seven.

Without a loop, I would have to write the same lines of code over and over. The loop also lets the user choose **any** password length, without me knowing it in advance.

### 4. `random.choice()`: Picking a Random Item

`random.choice()` picks one random item from a list:

```python
random_letter = random.choice(letters)   # e.g. 'q'
```

Every item in the list has an equal chance of being chosen, and the same character can be picked more than once.

### 5. `.append()`: Adding Items to a List

The `.append()` method adds an item to the **end** of a list:

```python
combined_list.append(random_letter)
```

On each pass of the loop, a new random character is added to `combined_list`, so the list grows until it holds every character in the password.

### 6. `random.shuffle()`: Randomising the Order

`random.shuffle()` rearranges the items in a list into a random order:

```python
random.shuffle(combined_list)
# ['a', 'K', 'r', '7', '2', '#']  →  ['7', 'a', '#', 'K', '2', 'r']
```

`random.shuffle()` changes the original list **in place** and doesn't return a new one. So I wrote `random.shuffle(combined_list)` on its own line, not `combined_list = random.shuffle(combined_list)`, which would set the variable to `None`.

### 7. String Concatenation: Building the Password

Finally, a loop goes through the shuffled list and adds each character onto the end of a string using `+=`:

```python
password = ""
for end in combined_list:
    password += end
```

The loop starts with an **empty string** `""` and adds one character on each pass. By the end, it has built the full password, e.g. `"" → "7" → "7a" → "7a#"…`.

This kind of `for` loop goes through **the items of a list** directly. The loops in section 3 go through **a range of numbers** instead.

### 8. The Newline Character `\n`

The `\n` at the end of each question moves the cursor onto a new line. The user therefore types their answer underneath the question rather than beside it:

```python
nr_letters = int(input("How many letters would you like in your password?\n"))
```

---

## What I Learned

This project helped me understand how loops can automate repetitive tasks and how randomness can make a program's output unpredictable.

Key learning outcomes include:

- Importing and using Python's built-in `random` module.
- Creating and storing data in lists.
- Using `for` loops with `range()` to repeat code a chosen number of times.
- Looping directly through the items of a list.
- Picking random items with `random.choice()`.
- Adding items to a list with `.append()`.
- Randomising the order of a list with `random.shuffle()`, and understanding that it changes the list in place.
- Building a string step by step with `+=`.
- Converting user input to integers with `int()`.
- Thinking about **security**: why a shuffled password is stronger than one that follows a predictable pattern.

The most important lesson was the power of **loops**. Instead of writing the same instructions repeatedly, a loop runs them as many times as needed. This makes the program shorter and easier to maintain, and lets it adapt to whatever the user enters.

---

## Future Improvements

Possible extensions to the project include:

- **Stronger security with the `secrets` module:** Python's `random` module is designed for things like games and simulations, not security. The built-in `secrets` module is designed for generating secure passwords and would be a better choice in a real-world tool.
- **Use the `string` module:** replace the long, hand-typed lists with `string.ascii_letters`, `string.digits` and `string.punctuation`.
- **Use `"".join()`:** build the password in one line with `password = "".join(combined_list)` instead of a loop.
- **Input validation:** ask the user to try again if they enter something that isn't a whole number, instead of the program crashing.
- **Minimum password length:** warn the user if their password is too short to be secure, e.g. under 12 characters.
- **Password strength checker:** rate the generated password as weak, medium or strong.
- **Generate several passwords:** let the user choose how many passwords to create at once.
- **Copy to clipboard:** automatically copy the password, ready to paste.
- **Functions:** move each step into its own reusable function to improve organisation.

These improvements would build on the existing program and give me the chance to practise more advanced Python concepts, such as additional modules and functions.

---

## Files

| File | Description |
|------|-------------|
| `main.py` | The PyPassword Generator program |
| `index.html` | Runs the program in a web browser using Pyodide |

---

## Course Context

This project was completed as part of **Day 5** of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 5 focuses on **`for` loops, the `range()` function and code blocks**. The PyPassword Generator brings these together with what I learned on Day 4 about **randomisation and lists** to build a practical, security-focused tool. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.