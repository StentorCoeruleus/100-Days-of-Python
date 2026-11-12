# Treasure Island: Python Adventure Game

## Overview

**Treasure Island** is a text-based adventure game developed in Python as the final project for **Day 3** of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

The game places the player on a quest to find hidden treasure on a mysterious island. Throughout the adventure, the player encounters a series of obstacles and must make decisions that determine how the story unfolds. Rather than using graphical environments or animated characters, the game runs entirely in the terminal. The player interacts with it by entering text-based choices, and the program responds to the decisions made. The objective of the game is to navigate the island successfully and find the treasure without falling into one of the traps along the way.

The game demonstrates how **conditional logic** can be used to create an interactive experience in which different choices lead to different outcomes.

---

## How to Play

There are three ways to try Treasure Island.

### Option 1: Play in your browser (no installation)

**[Launch Treasure Island](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%203/Treasure%20Island%20Project/)**

This runs the Python code directly in your web browser using [Pyodide](https://pyodide.org/). Click **Start**, type your choices into the box, and press **Enter**.

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
   cd "100-Days-of-Python/Day 3/Treasure Island Project"
   ```
3. Run the Python script:
   ```bash
   python task.py
   ```
   On macOS or Linux, you may need to type `python3 task.py` instead.
4. Follow the on-screen prompts and enter your choices to play the game.

### Option 3: Run it in an online Python editor

If you don't want to install anything, open `task.py` on GitHub, copy the code, and paste it into a free online Python editor such as [Programiz](https://www.programiz.com/python-programming/online-compiler/) or [Online-Python](https://www.online-python.com/). Then click **Run**.

---

## How the Game Works

The game follows a **branching narrative** structure. At each stage, the player is presented with a situation and must choose between the available options. The program evaluates the player's input and determines which part of the adventure should happen next. A correct decision allows the player to continue, while an incorrect decision leads to a game-over outcome.

### 1. Starting the Adventure

When the program starts, the player is introduced to the island of Nyxos and the objective of finding the treasure. The game uses text and ASCII art to establish the setting and create a simple visual representation of the adventure within the terminal. The player then begins making decisions that determine their route through the island.

### 2. Making Decisions

At each decision point, the player is presented with a choice. The options represent different actions the player can take to progress through the adventure. For example, for the first choice, the player must decide whether to turn left or right when the path splits into two. The program collects the player's response using Python's `input()` function. The response is then evaluated using conditional statements to determine the next stage of the game.

### 3. Following the Correct Path

The player's choices determine whether they can continue their journey.

If the player selects the correct option, the program moves them forward to the next challenge. For example, by turning left, the player progresses through the game and comes across the next obstacle. If they select an incorrect option, the player dies and receives a **Game Over**, ending the adventure. This branching structure means that the player's decisions, rather than random events, determine the outcome.

### 4. Winning or Losing

The adventure concludes when the player either reaches the treasure or encounters a fatal obstacle.

- **Victory:** the player makes the necessary decisions to reach the hidden treasure.
- **Game over:** the player makes a choice that leads to an unsuccessful outcome.

The game illustrates how a relatively small Python program can produce multiple possible outcomes through conditional logic.

### Example

```
Welcome to Treasure Island.
Your mission is to find the treasure.

You have arrived at the island of Nyxos. You are in a thick forest amidst heavy fog.
However, you notice that the path has split into two.
Do you go left or right? Type in your answer.
left
You continue down the path and come to the edge of a large lake.
Do you swim across or wait and build a raft? Type swim or wait.
swim
You decided to swim and were eaten alive by piranhas. Game Over.
```

---

## Game Flow

The Treasure Island project follows this sequence:

1. **Start:** the player begins the treasure hunt.
2. **First decision:** the player chooses whether to go left or right where the path splits.
3. **Second decision:** the player chooses whether to swim across the lake or wait and build a raft.
4. **Final challenge:** the player must pick the correct trapdoor (red, yellow or blue) to reach the treasure.
5. **Outcome:** the game displays either a winning message or a game-over message.

Each stage depends on the player's previous choice. The player must therefore follow the correct sequence of decisions to complete the adventure successfully.

---

## Python Concepts Used

This project introduces several fundamental Python programming concepts.

### 1. `print()`: Displaying Information

The `print()` function displays text in the terminal. It is used to introduce the game, describe the player's surroundings, present choices, and communicate the consequences of each decision.

```python
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
```

These statements provide the player with instructions and establish the objective of the game. The `\n` creates a new line, so a single `print()` can display text across several lines.

### 2. `input()` and Variables: Collecting Player Responses

The `input()` function pauses the program and waits for the player to enter a response:

```python
trapdoor = input("Pick which door to enter. Type red, yellow, or blue.\n")
```

The player's response is stored in a variable called `trapdoor`, which the program can use later to decide what happens next. By combining variables, the `input()` function and conditional statements, the program becomes interactive rather than simply displaying a fixed sequence of messages.

### 3. Conditional Statements: `if`, `elif` and `else`

The Treasure Island game uses conditional statements to direct the player along different paths. Conditional statements allow the program to run different blocks of code depending on whether particular conditions are met.

```python
path = input("Do you go left or right? Type in your answer.\n").lower()

if path == "right":
    print("You have fallen into a ravine. Game Over.")
elif path == "left":
    print("You continue down the path and come to the edge of a large lake.")
    # (Adventure continues...)
else:
    print("You continued past the path and fell into a ravine. Game Over.")
```

In this example, the program compares the input value with each condition to decide which indented block of code to run. If the input matches a condition, that condition's indented code runs. Any value that doesn't match the `if` or `elif` condition is handled by the `else` statement.

I used a third condition for a choice with only two options. This means the game still responds if the player types something other than `left` or `right`. I built that into the story: the player goes past the path and gets a Game Over.

I also used the `.lower()` function to handle the player typing `left` or `right` with capital letters (e.g. `LEFT` or `Right`). It converts all the characters to lowercase so the code can recognise them. The result is more polished code and smoother gameplay.

### 4. Nested Conditional Statements

A **nested conditional** is a conditional statement placed inside another conditional statement. This allows the program to evaluate decisions in stages.

```python
path = input("Do you go left or right? Type in your answer.\n").lower()

if path == "right":
    print("You have fallen into a ravine. Game Over.")
elif path == "left":
    print("You continue down the path and come to the edge of a large lake.")
    lake = input("Do you swim across or wait and build a raft? Type swim or wait.\n").lower()
    if not lake == "wait":
        print("You decided to swim and were eaten alive by piranhas. Game Over.")
    else:
        print("You manage to get across the lake and enter a cave.\nThere are three trapdoors: red, yellow, and blue.")
        trapdoor = input("Pick which door to enter. Type red, yellow, or blue.\n")
else:
    print("You continued past the path and fell into a ravine. Game Over.")
```

In this example, the second decision is only evaluated if the player makes the correct first choice. Nested conditionals are useful for creating branching adventures because later decisions depend on earlier ones. **Indentation** is crucial here, because it makes sure each response is linked to the correct input.

### 5. Logical Operators

Python's logical operators allow multiple conditions to be combined or evaluated together. The two logical operators used are:

- **`or`:** evaluates to `True` when at least one condition is true.
- **`not`:** reverses a Boolean value.

**Example 1: `or`**

```python
trapdoor = input("Pick which door to enter. Type red, yellow, or blue.\n")

if trapdoor == "Yellow" or trapdoor == "yellow":
    print("You found King Midas' treasure. Congratulations, you win!")
```

**Example 2: `not`**

```python
lake = input("Do you swim across or wait and build a raft? Type swim or wait.\n").lower()

if not lake == "wait":
    print("You decided to swim and were eaten alive by piranhas. Game Over.")
else:
    print("You manage to get across the lake and enter a cave.\nThere are three trapdoors: red, yellow, and blue.")
```

In the first example, the indented code runs whether the user types `yellow` or `Yellow`, because either condition being `True` is enough. In the second example, if the player types `wait`, then `lake == "wait"` is `True`, so `not lake == "wait"` becomes `False` and the `else` statement runs instead.

Logical operators are useful for more complex decision-making, although a simple version of Treasure Island can be implemented primarily with `if`, `elif` and `else` statements.

### 6. ASCII Art and Raw Strings

**ASCII art** uses ordinary text characters to create simple illustrations in the terminal. The game opens with an ASCII art picture of the treasure island, which adds visual interest without needing a graphics library or a graphical user interface.

The art is written as a **multi-line string** using triple quotes (`'''`), so it can span several lines and keep its shape. Because the art contains a backslash (`\`), I used a **raw string**, marked by the `r` prefix:

```python
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
...
''')
```

In a normal string, Python treats a backslash as the start of an **escape sequence** (like `\n` for a new line). Without the `r`, recent versions of Python display a `SyntaxWarning: invalid escape sequence` message. With a raw string, the backslash is displayed exactly as typed.

---

## What I Learned

This project helped reinforce the fundamentals of Python programming by applying them to a small interactive game.

Key learning outcomes include:

- Using `print()` and `input()` to create a text-based user interaction.
- Storing user responses in variables.
- Using comparison operators (`==`) to evaluate conditions.
- Controlling program execution with `if`, `elif` and `else` statements.
- Building branching logic with nested conditional statements.
- Understanding how logical operators (`or`, `not`) combine and reverse Boolean conditions.
- Using `.lower()` to handle uppercase input.
- Using indentation to define blocks of code.
- Displaying simple visual elements with ASCII art and raw strings.
- Translating a sequence of rules and decisions into a working program.

The most important lesson is that a program does not always need to run from top to bottom in a single fixed sequence. Conditional statements allow it to respond differently depending on the information it receives.

---

## Future Improvements

Possible extensions to the project include:

- **Consistent input handling:** use `.lower()` on the trapdoor choice too, as I did for the first two decisions. Then `YELLOW` or `yElLoW` would also work, and the `or` checks would no longer be needed.
- **Replay functionality:** allow the player to restart the adventure after winning or losing.
- **More branching paths:** introduce additional decisions, obstacles and endings.
- **Inventory system:** allow the player to collect items and use them to overcome obstacles.
- **Functions:** separate sections of the game into reusable functions to improve organisation.
- **Random events:** introduce randomness to make different playthroughs less predictable.

These improvements could build on the existing program while providing opportunities to practise more advanced Python concepts.

---

## Files

| File | Description |
|------|-------------|
| [`task.py`](task.py) | The Treasure Island game |
| `index.html` | Runs the game in a web browser using Pyodide |

---

## Course Context

This project was completed as part of **Day 3** of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 3 focuses on **conditional statements, logical operators and control flow**, with the Treasure Island project providing a practical application of decision-making in Python. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.