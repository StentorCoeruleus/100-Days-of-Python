# Blackjack: Python Card Game

## Overview

Blackjack is a text-based card game I built in Python as the capstone project for Day 11 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

The player plays against the computer, which acts as the dealer. Each side is dealt two cards, and the player decides whether to take more cards (*hit*) or keep their hand (*stand*). The aim is to finish with a score closer to 21 than the computer's without going over. Once the player has finished, the computer draws cards until it reaches at least 17, and the two hands are compared to decide the winner.

The game runs entirely in the terminal and opens with an ASCII art logo. Unlike my earlier projects, I wrote this one in two stages. First, I wrote a full working draft without any functions. Then I went back over it, fixed the bugs I found, and refactored it into reusable functions. This README describes the finished game and the process that got me there.

---

## How to Play

There are three ways to try Blackjack.

### Option 1: Play in your browser (no installation)

**[Launch Blackjack](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%2011/task/)**

This runs the Python code directly in your web browser using [Pyodide](https://pyodide.org/). Click **Start**, type your choices into the box, and press **Enter**.

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
   cd "100-Days-of-Python/Day 11/task"
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```
   On macOS or Linux, you may need to type `python3 main.py` instead.
4. Type `ENTER` to start a game, then follow the on-screen prompts.

**Important:** keep `main.py` and `art.py` in the **same folder**. `main.py` imports the logo from `art.py`, so the game won't run without it.

### Option 3: Run it in an online Python editor

Because this game is split across two files, it needs an online editor that supports multiple files, such as [Replit](https://replit.com/). Create a new Python project, add `art.py` as an extra file, paste in the code for both files, and click **Run**.

---

## Game Rules

The game uses the simplified house rules from the course:

- The deck is unlimited, and every card is equally likely to be drawn. Cards are not removed from the deck once they are dealt.
- Cards are represented by their values: `2` to `10`, with `10` appearing four times to stand for 10, Jack, Queen and King.
- An Ace (`11`) counts as 11, or as 1 if counting it as 11 would take the score over 21.
- A Blackjack is an Ace and a 10-value card as the first two cards. It beats any other hand, including a 21 made with three or more cards.
- If both the player and the computer have Blackjack, the game is a draw.
- If the player goes over 21, they are bust and lose immediately, even if the computer would also have gone bust.
- The computer must keep drawing cards until its score is at least 17.

---

## How the Game Works

### 1. Starting the Game

The program asks the player whether they want to play. Typing `ENTER` starts a game, `EXIT` quits, and anything else displays a message and asks again. Input is converted to uppercase with `.upper()`, so `enter`, `Enter` and `ENTER` all work.

### 2. Dealing the Cards

The screen is cleared, the logo is displayed, and two random cards are dealt to each side. The player can see both of their own cards and their score, but only the computer's first card.

### 3. Checking for Blackjack

If either side has Blackjack, the game skips straight to the result. Neither the player nor the computer draws any more cards.

### 4. The Player's Turn

The player types `HIT` to draw another card or `STAND` to keep their hand. After each card, the score is recalculated:

- If the score is under 21, the updated hand is shown and the player chooses again.
- If the score reaches exactly 21, the player's turn ends automatically.
- If the score goes over 21 and the hand contains an Ace counted as 11, that Ace becomes a 1.
- If the score is still over 21, the player is bust and the computer doesn't take its turn.

Any other input displays a message and asks again.

### 5. The Computer's Turn

If the player hasn't gone bust, the computer keeps drawing cards until its score is at least 17. Its Aces are handled in the same way as the player's.

### 6. The Showdown

Both final hands are revealed, and the game compares the scores to decide the winner. The player is then asked whether they want to play again.

### Example

```
Would you like to play a game of Blackjack?
Type 'ENTER' to start, or 'EXIT' to quit.
enter
My cards: [10, 6], current score: 16
Computer's first card: 9
Type 'HIT' to get another card, or 'STAND' to pass.
hit
My cards: [10, 6, 4], current score: 20
Computer's first card: 9
Type 'HIT' to get another card, or 'STAND' to pass.
stand
Your final hand: [10, 6, 4], final score: 20
Computer's final hand: [9, 5, 10], final score: 24
You Win!
Would you like to play a game of Blackjack?
Type 'ENTER' to start, or 'EXIT' to quit.
exit
```

---

## Game Flow

1. **Start:** the player types `ENTER` to play or `EXIT` to quit.
2. **Deal:** two cards are dealt to each side, and the computer's first card is shown.
3. **Blackjack check:** if either side has Blackjack, the game goes straight to the showdown.
4. **Player's turn:** the player hits or stands until they stand, reach 21 or go bust.
5. **Computer's turn:** unless the player is bust, the computer draws until it has at least 17.
6. **Showdown:** both hands are revealed and the result is displayed.
7. **Repeat or end:** the loop repeats until the player types `EXIT`.

Two Boolean flags, `dealing_cards` and `computer_turn`, control whether the player's turn and the computer's turn take place. A third flag, `game_running`, keeps the whole game going between rounds.

---

## Modular Code

The project is split across these files:

| File | Description |
|------|-------------|
| [`main.py`](main.py) | The final version of the game: the three functions and the main game loop |
| [`art.py`](art.py) | The ASCII art Blackjack logo |
| [`draft.py`](draft.py) | My first full draft, written before refactoring into functions |
| `index.html` | Runs the game in a web browser using Pyodide |

Keeping the logo in `art.py` keeps `main.py` focused on the game's logic. I've kept `draft.py` in the repository so the two versions can be compared.

---

## From Draft to Final Version: My Process

For this project I set myself a two-stage approach:

1. **Write the whole game in full**, without functions, so I could focus on getting the rules right.
2. **Go back over it and simplify it**, by spotting repeated code and moving it into functions.

Both stages taught me a lot, mainly through the bugs I found along the way.

### Stage 1: The Draft

#### Bug 1: `and` doesn't work the way it reads in English

To end the game early when someone had Blackjack, I first wrote:

```python
if 10 and 11 in computer_cards:
    dealing_cards = False
```

I meant "if 10 and 11 are both in the computer's cards". Python reads it as:

```python
if (10) and (11 in computer_cards):
```

Each side of `and` is checked separately. A non-zero number on its own is always **truthy**, so `10` always counts as `True`, and the condition only checked whether the computer had an Ace. In one test, the computer was dealt `[11, 4]` and I never got the chance to hit or stand. I fixed it by writing out the full check on both sides:

```python
if 10 in computer_cards and 11 in computer_cards:
```

Later I replaced it with an even simpler check: a Blackjack is just a score of 21 with two cards.

This was the same lesson as the truthiness bug in my Day 10 Calculator, so I'm now much more careful about conditions that "read" correctly but don't compare anything.

#### Bug 2: The computer's Aces were never counted as 1

My draft converted the player's Aces from 11 to 1, but I hadn't written the same logic for the computer. In one game the computer finished on `[11, 4, 11]`, a score of 26, when it should have counted one Ace as 1 (a score of 16) and drawn again. I added the same Ace check inside the computer's drawing loop.

#### Bug 3: Typing `EXIT` didn't quit

Nothing ever set `game_running` to `False`, so typing `EXIT` just asked the question again. I added an `elif` for `EXIT` and an `else` for invalid input.

#### Bug 4: Two Aces in the opening hand

If the first two cards were `[11, 11]`, the score was 22. For the computer, 22 is already at least 17, so its drawing loop never ran and the Ace was never converted. I added a check straight after the deal. I also worked out that only **one** Ace needs to change: `[11, 1]` scores 12, which is better than `[1, 1]`, which scores 2. The second Ace stays at 11 until it's needed.

At first I wrote this check with `if` for the computer and `elif` for the player. That meant that if **both** sides were dealt two Aces, only the computer's hand was fixed. Changing the `elif` to a separate `if` solved it, because the two checks don't depend on each other.

#### Bug 5: Getting the results right

The order of an `if` / `elif` chain matters, because only the first matching condition runs. Several bugs came from this:

- If both sides had Blackjack, the computer's Blackjack was checked first, so the player lost when it should have been a draw.
- When I fixed that with a general "both have 21" check, a player's Blackjack only drew against the computer's three-card 21, when Blackjack should win. I used `len()` to check that both hands had exactly two cards.
- That fix then made an ordinary 21 against 21 (three cards each) fall through to a "You lose!" line. Rather than add another condition, I deleted the extra 21 checks. The general comparisons further down the chain already handled every 21 case correctly.

#### Bug 6: A fix that caused a new bug

While moving the "exactly 21" check below the Ace conversion, I accidentally deleted the line that ended the player's turn when they went bust. The player could keep drawing cards after going over 21. I fixed it by ending the turn whenever the score was 21 or more:

```python
if my_score >= 21:
    dealing_cards = False
```

In the same round of changes, I also made a typo so the computer's Blackjack printed "You win!". These taught me to re-test the whole game after every change, not just the part I had just edited.

### Stage 2: Refactoring into Functions

Once the draft worked, I looked for code that was repeated. The biggest problem was the Ace conversion, which appeared in four places: the computer's opening hand, the player's opening hand, the player's turn and the computer's turn. Several of the bugs above came from fixing one copy and forgetting another.

I replaced the repeated code with three functions:

| Function | What it does |
|----------|--------------|
| `random_card()` | Returns a random card from the deck |
| `calculate_score(value)` | Adds up a hand, converts an Ace from 11 to 1 if needed, and returns `0` for a Blackjack |
| `showdown(computer, user)` | Compares the final scores and prints the result |

#### What I learned about parameters: lists vs integers

My first attempt at a function looked like this:

```python
def deal_card(card, score):
    dealt_card = random.choice(cards)
    card.append(dealt_card)
    score += dealt_card
```

When I ran it, the hands filled up with cards, but the scores stayed at 0. The reason is the difference between a list and an integer:

- A list can be changed in place. `card` points to the same list as `my_cards`, so `.append()` changes the original list.
- An integer can't be changed in place. `score += dealt_card` creates a new number and points the local name `score` at it. The original `my_score` still points to `0`, and the new value is thrown away when the function ends.

I considered using the `global` keyword instead, but that would have meant writing a separate function for each player, which is the repetition I was trying to remove. Instead, I stopped keeping a running score at all. `calculate_score()` works out the score from the hand and returns it:

```python
my_score = calculate_score(my_cards)
```

#### One last bug: `+=` vs `=`

At first I kept `+=` from the draft:

```python
my_score += calculate_score(my_cards)
```

Because `calculate_score()` already returns the total of the **whole** hand, this added the full total on top of the previous score. A hand of `[5, 6, 3]` (14) was shown as 25. Changing `+=` to `=` fixed it. The score is now recalculated from the hand every time, so it can never get out of step with the cards.

#### Other tidying

- I moved the functions and the `cards` list above the main loop, so they are created once instead of at the start of every game.
- I removed the "Ace Detected!" messages, which had given away that the computer was holding Aces.
- I used a `computer_turn` flag so the computer doesn't draw cards after the player has already gone bust or someone has Blackjack.

---

## Python Concepts Used

This project brings together the concepts from Days 1 to 10 of the course.

### 1. Lists and `random.choice()`

The deck is a list of card values, and `random.choice()` picks one at random:

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card():
    return random.choice(cards)
```

Each hand is also a list, and new cards are added with `.append()`:

```python
my_cards.append(random_card())
```

### 2. Functions with Outputs: `return`

`calculate_score()` takes a hand as its input and returns its score:

```python
def calculate_score(value):
    if sum(value) == 21 and len(value) == 2:
        return 0
    elif sum(value) > 21:
        if 11 in value:
            value.remove(11)
            value.append(1)
            return sum(value)
        else:
            return sum(value)
    else:
        return sum(value)
```

Because one function handles the scoring for both players, the Ace logic only has to be written, and fixed, once.

### 3. Using `0` as a Special Value

`calculate_score()` returns `0` for a Blackjack. No real hand can score 0, so it works as a signal that is easy to check:

```python
if computer_score == 0 or my_score == 0:
    dealing_cards = False
    computer_turn = False
```

### 4. `sum()`, `len()`, `.remove()` and `in`

- `sum(value)` adds up every card in a hand.
- `len(value)` counts the cards, which separates a two-card Blackjack from a 21 made with more cards.
- `11 in value` checks whether the hand contains an Ace counted as 11.
- `.remove(11)` removes the first 11 from the hand, and `.append(1)` adds a 1 in its place.

### 5. `while` Loops and Boolean Flags

The game uses three Boolean flags:

```python
game_running = True     # keeps the whole program going between games
dealing_cards = True    # keeps the player's turn going
computer_turn = True    # decides whether the computer draws cards
```

The computer's turn uses a `while` loop with a condition instead of a flag. It keeps drawing for as long as its score is under 17:

```python
if computer_turn:
    while computer_score < 17:
        computer_cards.append(random_card())
        computer_score = calculate_score(computer_cards)
```

### 6. Logical Operators

`and` and `or` combine conditions, but each side must be a complete comparison. `if 10 and 11 in computer_cards:` was the source of my first bug, as explained above. The working version uses complete conditions on both sides:

```python
if sum(value) == 21 and len(value) == 2:
```

### 7. Ordering an `if` / `elif` Chain

`showdown()` checks the most specific cases first (Blackjacks and busts) and the general comparisons last:

```python
def showdown(computer, user):
    if computer == 0 and user == 0:
        print("It's a draw!")
    elif computer == 0:
        print("Computer has Blackjack! You Lose!")
    elif user == 0:
        print("You have Blackjack! You Win!")
    elif user > 21:
        print("Bust! You Lose!")
    elif computer > 21:
        print("You Win!")
    elif computer == user:
        print("It's a draw!")
    elif computer > user:
        print("You Lose!")
    elif user > computer:
        print("You Win!")
```

The player's bust is checked before the computer's, so a bust player always loses.

### 8. `.upper()`: Handling Mixed-Case Input

All input is converted to uppercase, so `hit`, `Hit` and `HIT` all work:

```python
another_card = input("Type 'HIT' to get another card, or 'STAND' to pass.\n").upper()
```

### 9. Importing a Module and Clearing the Screen

The logo is stored in `art.py` and imported at the top of `main.py`. At the start of each game, the screen is cleared by printing 100 new lines:

```python
print("\n" * 100)
print(art.logo)
```

---

## What I Learned

This was my biggest project so far, and the first one where I wrote a full draft myself before refactoring it.

Key learning outcomes include:

- Turning a set of written rules into a working program.
- Writing a full draft first, then improving it, rather than trying to write perfect code straight away.
- Writing functions that take parameters and return values.
- Understanding that lists can be changed inside a function but integers can't.
- Choosing `return` values over the `global` keyword.
- Recalculating a value from its source (`=`) instead of adding to it (`+=`).
- Understanding why `10 and 11 in cards` doesn't mean "both 10 and 11 are in the list".
- Using `sum()`, `len()`, `in`, `.append()` and `.remove()` with lists.
- Using Boolean flags to control which parts of the game run.
- Ordering an `if` / `elif` chain so the most specific cases are checked first.
- Re-testing the whole program after every change, because fixing one bug can cause another.

The most important lesson was the value of removing repeated code. When the Ace logic was copied in four places, I kept fixing one copy and missing another. Once it lived in a single function, I only had to get it right once.

---

## Future Improvements

These changes wouldn't affect the result of a game, so I've listed them here for a future version:

- **Show "Blackjack!" instead of a score of 0:** a Blackjack is currently displayed as `current score: 0`, which could confuse players. The program could print `Blackjack!` (or the real score of 21) whenever `calculate_score()` returns 0.
- **Keep Aces in their original position:** when an Ace is converted, `.remove()` and `.append()` move it to the end of the hand, so `[11, 5, 10]` is shown as `[5, 10, 1]`. Replacing it in place with `value[value.index(11)] = 1` would keep the cards in the order they were dealt.
- **Handle any number of Aces:** `calculate_score()` converts at most one Ace each time it's called. This is enough here, because it runs after every new card, but a `while` loop would make it correct for any hand:
  ```python
  while sum(value) > 21 and 11 in value:
      value[value.index(11)] = 1
  ```
- **Clearer function and parameter names:** for example, `hand` instead of `value`, and `deal_card()` instead of `random_card()`.
- **Docstrings:** add a short description to each function explaining what it does.
- **Show card names:** display Aces, Jacks, Queens and Kings as `A`, `J`, `Q` and `K` instead of numbers.
- **A real deck:** use a 52-card deck and remove cards as they are dealt, so the odds change during a game like they would in a casino.
- **Betting:** give the player a balance of chips to bet on each hand.
- **More player options:** add common Blackjack moves such as **doubling down** and **splitting** pairs.

These improvements would give me the chance to practise more advanced Python concepts, such as list indexing, docstrings and dictionaries.

---

## Course Context

This project was completed as part of Day 11 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 11 is the course's first capstone project. Instead of introducing new concepts, it brings together everything from the beginner section: variables, lists, conditional statements, loops, functions with outputs and imported modules. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.