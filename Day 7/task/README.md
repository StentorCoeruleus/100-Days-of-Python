# Hangman: Python Word-Guessing Game

## Overview

**Hangman** is a text-based word-guessing game I built in Python as the final project for **Day 7** of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

The game is based on the classic pen-and-paper game. The computer picks a secret word at random, and the player tries to work it out by guessing one letter at a time. Each correct guess reveals that letter wherever it appears in the word. Each wrong guess costs the player a life and adds another part to the hangman drawing. The player wins by revealing the whole word before they run out of lives.

The game runs entirely in the terminal. It uses ASCII art to draw the game logo and the hangman at each stage, and the player interacts by typing letters. The project brings together everything I had learned in the first week of the course, including loops, conditionals, lists, randomisation and modules, to build a complete, replayable game.

---

## How to Play

There are three ways to try the Hangman game.

### Option 1: Play in your browser (no installation)

**[Launch Hangman](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%207/task/)**

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
   cd "100-Days-of-Python/Day 7/task"
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```
   On macOS or Linux, you may need to type `python3 main.py` instead.
4. Follow the on-screen prompts and guess the word.

**Important:** keep `main.py`, `hangman_words.py` and `hangman_art.py` in the **same folder**. `main.py` imports the other two files, so the game won't run without them.

### Option 3: Run it in an online Python editor

Because this game is split across three files, it needs an online editor that supports multiple files, such as [Replit](https://replit.com/). Create a new Python project, add `hangman_words.py` and `hangman_art.py` as extra files, paste in the code for all three files, and click **Run**.

---

## How the Game Works

The game follows a **game loop** structure. It sets up the game once, then repeats the same steps (ask for a guess, check it, update the display) until the player either wins or loses.

### 1. Starting the Game

When the program starts, it displays the Hangman logo in ASCII art and a welcome message. The player starts with **6 lives**.

### 2. Choosing the Secret Word

The program picks a random word from a list of over 200 words stored in `hangman_words.py`. It then shows the player a row of blanks, one for each letter, so they know how long the word is. For example, a five-letter word appears as `_____`.

### 3. Guessing a Letter

The player is shown how many lives they have left and asked to guess a letter. Their guess is converted to lowercase, so `A` and `a` are treated the same.

If the player has already guessed that letter, the game reminds them.

### 4. Revealing the Word

The program checks every letter of the secret word, one at a time:

- If the letter matches the guess, it is revealed.
- If the letter was correctly guessed in an earlier turn, it stays revealed.
- Otherwise, it stays hidden as `_`.

The updated word is then displayed, e.g. `__zz_`.

### 5. Losing a Life

If the guessed letter isn't in the word, the player is told and loses a life. The hangman drawing updates to show the next stage.

### 6. Winning or Losing

The game ends in one of two ways:

- **Victory:** the player reveals every letter in the word before running out of lives, and the game displays **YOU WIN**.
- **Game over:** the player loses all 6 lives. The hangman drawing is complete, the game displays **YOU LOSE**, and the secret word is revealed.

### Example

```
Welcome to the Hangman Game!
Word to guess: _____
****************************6/6 LIVES LEFT****************************
Guess a letter: z
Word to guess: __zz_
****************************6/6 LIVES LEFT****************************
Guess a letter: e
Word to guess: __zz_
e is not in the word. You lose a life.
****************************5/6 LIVES LEFT****************************
Guess a letter: j
Word to guess: j_zz_
```

*The hangman drawing is displayed after every guess, showing one more body part for each life lost.*

---

## Game Flow

1. **Start:** the game displays the logo and a welcome message, and gives the player 6 lives.
2. **Word selection:** a random word is chosen and shown as blanks.
3. **Guess:** the player enters a letter.
4. **Check:** the program checks the guess against every letter of the word.
5. **Update:** correct letters are revealed. A wrong guess costs a life.
6. **Display:** the updated word and the current hangman drawing are shown.
7. **Repeat:** steps 3–6 repeat until the game ends.
8. **Outcome:** the game displays either a winning message or a game-over message.

My Day 3 Treasure Island game moved through a fixed sequence of decisions. Hangman is different: it **repeats** the same steps an unknown number of times, until a win or loss condition is met. This is the key difference between a program that runs from top to bottom once and a **game loop**.

---

## Modular Code

The project is split across three files, so each one has a single, clear job:

| File | Description |
|------|-------------|
| [`main.py`](main.py) | The game logic: the game loop, guesses, lives, and win/lose checks |
| [`hangman_words.py`](hangman_words.py) | The list of over 200 words the game chooses from |
| [`hangman_art.py`](hangman_art.py) | ASCII art: the game logo and the 7 stages of the hangman drawing |
| `index.html` | Runs the game in a web browser using Pyodide |

Keeping the data (the words and art) separate from the logic makes `main.py` much shorter and easier to read. It also makes the game easy to change. For example, I could add new words without touching the game logic at all.

---

## Python Concepts Used

This project combines many of the Python concepts from the first week of the course, focusing on **`while` loops**, **lists**, **conditionals** and **modules**.

### 1. Importing Modules: Built-in and My Own

As well as importing Python's built-in `random` module, I imported **my own Python files** as modules:

```python
import random
import hangman_words
import hangman_art
```

Once imported, I can use anything defined in those files by putting the file name in front of it:

```python
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
```

This taught me how larger programs are organised: code is split into separate files that work together.

### 2. `random.choice()`: Picking the Secret Word

`random.choice()` picks one random item from a list, so the game uses a different word each time it is played:

```python
chosen_word = random.choice(hangman_words.word_list)
```

### 3. `len()` and `range()`: Creating the Blanks

To show the player how long the word is, the program needs one `_` for each letter. `len()` counts the letters in the word, and a `for` loop with `range()` adds an underscore for each one:

```python
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
```

For a five-letter word, `len()` returns `5`, so the loop runs 5 times and builds `"_____"`.

### 4. `while` Loops and Boolean Flags: The Game Loop

A `while` loop keeps repeating **as long as a condition is true**. This makes it ideal for a game, because nobody knows in advance how many guesses the player will need.

```python
game_over = False

while not game_over:
    # ask for a guess, check it, update the display...
```

`game_over` is a **Boolean flag**, a variable that is either `True` or `False`. It starts as `False`, so `not game_over` is `True` and the loop keeps running. When the player wins or loses, the program sets `game_over = True`, and the loop stops.

```python
if lives == 0:
    game_over = True

if "_" not in display:
    game_over = True
```

A `for` loop is best when you know how many times to repeat something, like the password length in Day 5. A `while` loop is best when you **don't** know.

### 5. `.lower()`: Handling Uppercase Input

The player's guess is converted to lowercase as soon as it is entered:

```python
guess = input("Guess a letter: ").lower()
```

All the words in the word list are lowercase. Without `.lower()`, a guess of `A` would never match the `a` in the word.

### 6. Looping Through a String

A `for` loop can go through a **string** one character at a time, just like a list. The program uses this to compare the player's guess with each letter of the secret word:

```python
for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```

The `display` string is rebuilt from scratch on every turn:

- **`if`:** the letter matches this guess, so it is revealed.
- **`elif`:** the letter was correctly guessed in an earlier turn, so it stays revealed.
- **`else`:** the letter hasn't been guessed yet, so it stays hidden as `_`.

The `elif` is important. Without it, correctly guessed letters would disappear again on the next turn.

### 7. Lists and `.append()`: Remembering Guesses

The game uses two lists to remember what has happened so far:

```python
correct_letters = []
guesses = []
```

- `correct_letters` stores every correct guess, so revealed letters stay visible.
- `guesses` stores every guess the player has made, so the game can tell them if they repeat a letter.

New guesses are added to the end of the list with `.append()`:

```python
guesses.append(guess)
```

### 8. The `in` and `not in` Operators

The `in` operator checks whether a value exists inside a string or a list, and returns `True` or `False`. The game uses it in several places:

```python
if guess in guesses:                 # Has the player already guessed this letter?
if guess not in chosen_word:         # Is the guess wrong?
if "_" not in display:               # Has every letter been revealed?
```

This is much simpler than writing my own loop to search through the word or list each time.

### 9. Lives and the `-=` Operator

The player's lives are stored in a variable, and each wrong guess subtracts one:

```python
lives -= 1    # same as: lives = lives - 1
```

### 10. List Indexing: Choosing the Right Drawing

The 7 stages of the hangman drawing are stored in a list in `hangman_art.py`. They are ordered from the **finished** drawing at index `0` to the **empty** gallows at index `6`. Because of this order, the number of lives left can be used directly as the index:

```python
print(hangman_art.stages[lives])
```

| Lives left | Index | Drawing shown |
|-----------|-------|---------------|
| 6 | `stages[6]` | Empty gallows |
| 3 | `stages[3]` | Head, body and one arm |
| 0 | `stages[0]` | Complete hangman (game over) |

This avoids needing an `if` / `elif` statement for every possible number of lives.

### 11. Multi-line Strings, Raw Strings and ASCII Art

The logo and hangman drawings are written as **multi-line strings**, using triple quotes `'''`, so they can span several lines and keep their shape.

Some of them also use the `r` prefix to make a **raw string**:

```python
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', ...]
```

In a normal string, Python treats a backslash `\` as the start of an **escape sequence** (like `\n` for a new line). In a raw string, backslashes are displayed exactly as typed, which is essential for drawing the hangman's arms and legs.

### 12. f-Strings: Showing the Game Status

f-strings insert variables directly into messages, so the player always sees their current number of lives and whether their guess was right:

```python
print(f"****************************{lives}/6 LIVES LEFT****************************")
print(f"{guess} is not in the word. You lose a life.")
```

---

## What I Learned

This project helped me combine everything from the first week of the course into a single, complete game.

Key learning outcomes include:

- Splitting a program into **multiple files** and importing my own modules.
- Using a **`while` loop** with a **Boolean flag** to build a game loop.
- Understanding when to use a `while` loop instead of a `for` loop.
- Looping through a **string** character by character.
- Using lists to **store and remember** information between turns.
- Checking membership with the `in` and `not in` operators.
- Using `if`, `elif` and `else` to handle different outcomes.
- Using `.lower()` to make user input consistent.
- Using **list indexing** to link the number of lives to the correct drawing.
- Displaying ASCII art with multi-line and raw strings.
- **Breaking a large problem down** into smaller steps before writing any code.

The most important lesson was **problem decomposition**. Hangman is too big to write all at once. The course encouraged me to plan the game as a flowchart first, then build and test it one step at a time: choosing a word, checking a guess, revealing letters, tracking lives, and finally ending the game. This step-by-step approach is how real software is built.

---

## Future Improvements

Possible extensions to the project include:

- **Don't punish repeated guesses:** at the moment, guessing the same wrong letter twice costs two lives. The game could skip the rest of the turn with `continue` when a letter has already been guessed.
- **Input validation:** reject guesses that are longer than one character, or that aren't letters.
- **Show guessed letters:** display all the letters the player has already tried.
- **Replay functionality:** let the player start a new game without restarting the program.
- **Difficulty levels:** let the player choose easy, medium or hard, with shorter or longer words or more or fewer lives.
- **Hints:** reveal a letter or a clue in exchange for a life.
- **Word categories:** let the player choose a theme, such as animals, countries or science.
- **Functions:** move each step of the game into its own reusable function to improve organisation.

These improvements would build on the existing program and give me the chance to practise more advanced Python concepts, such as `continue`, input validation and functions.

---

## Course Context

This project was completed as part of **Day 7** of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 7 brings together everything from the first week of the course, including variables, conditionals, randomisation, lists, `for` loops and `while` loops, to build a complete game from scratch. The course also introduced **flowcharts** as a way to plan a program and break a complex problem into manageable steps before coding. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.