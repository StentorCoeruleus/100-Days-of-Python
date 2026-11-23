# Higher or Lower: Python Guessing Game
 
## Overview
 
Higher or Lower is a text-based guessing game I built in Python as the final project for Day 14 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.
 
The game shows the player two well-known people or brands and asks which one has more Instagram followers. If the player guesses correctly, they score a point. The screen is cleared, the account in position B moves up to position A, a new account is drawn for position B, and the game continues. One wrong guess ends the game, so the aim is to build the longest winning streak possible.
 
The game runs entirely in the terminal and uses ASCII art for its logo and "VS" graphic. The data for 50 accounts is stored in a separate file as a list of dictionaries. After finishing my first version, I reviewed it, found several bugs, and fixed them one at a time. This README describes the finished game and what I learned from that process.
 
---
 
## How to Play
 
There are three ways to try Higher or Lower.
 
### Option 1: Play in your browser (no installation)
 
**[Launch Higher or Lower](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%2014/Higher%20or%20Lower%20Project/)**
 
This runs the Python code directly in your web browser using [Pyodide](https://pyodide.org/). Python takes a few seconds to load. Then type your answer into the box at the bottom of the page and press *Enter*.
 
For the best experience, use **Chrome** or **Edge**. Other browsers, such as Firefox and Safari, ask for your answers in pop-up boxes instead.
 
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
cd "100-Days-of-Python/Day 14/Higher or Lower Project"
```
3. Run the Python script:
```bash
python main.py
```
   On macOS or Linux, you may need to type `python3 main.py` instead.
4. Type `A` or `B` to make each guess, then follow the on-screen prompts.
 
**Important:** keep `main.py`, `art.py` and `game_data.py` in the **same folder**. `main.py` imports the logo from `art.py` and the account data from `game_data.py`, so the game won't run without them.
 
### Option 3: Run it in an online Python editor
 
Because this game is split across three files, it needs an online editor that supports multiple files, such as [Replit](https://replit.com/). Create a new Python project, add `art.py` and `game_data.py` as extra files, paste in the code for all three files, and click *Run*.
 
---
 
## Game Rules
 
- Each round compares two accounts, labelled **A** and **B**.
- The player types `A` or `B` to choose the account they think has more followers.
- A correct guess scores one point. The screen is cleared, account B becomes the new account A, and a new account B is drawn.
- A wrong guess ends the game and shows the final score.
- If both accounts have the same number of followers, either answer counts as correct.
- Any answer other than `A` or `B` counts as a wrong guess.
- The same account never appears as both A and B.
---
 
## How the Game Works
 
### 1. Choosing the First Two Accounts
 
When a game starts, the program picks a random account for position A and a different random account for position B. Each account is shown with its name, a short description and its country, but not its follower count.
 
### 2. Making a Guess
 
The logo, both accounts and the "VS" graphic are displayed, and the player is asked who has more followers. Their answer is converted to uppercase with `.upper()`, so `a` and `A` both work.
 
### 3. Checking the Answer
 
The program compares the two follower counts with the player's choice:
 
- **Correct:** the screen is cleared, and the score goes up by one and is displayed at the top. Account B moves up to position A, and a new account is drawn for B.
- **Wrong:** the final score is displayed and the game ends.
### 4. Playing Again
 
After a game ends, the player is asked whether they want to play again. Typing `ENTER` clears the screen and starts a new game with the score reset to 0. Typing `EXIT`, or anything else, quits the program.
 
### Example
 
```
Compare A: Emma Watson, a Actress from United Kingdom
Against B: National Geographic, a Magazine from United States
Who has more followers? Type 'A' or 'B':
b
```
 
The screen clears, and the next round begins:
 
```
That's right!
Current score: 1
Compare A: National Geographic, a Magazine from United States
Against B: Kendall Jenner, a Reality TV personality and Model from United States
Who has more followers? Type 'A' or 'B':
a
Sorry, that's wrong.
Final score: 1
Would you like to play again? Type 'ENTER' to start or 'EXIT' to quit.exit
```
 
The logo and "VS" art have been left out of this example to keep it short.
 
---
 
## Game Flow
 
1. **Start:** two different accounts are drawn for positions A and B.
2. **Display:** the logo, both accounts and the "VS" graphic are shown.
3. **Guess:** the player types `A` or `B`.
4. **Check:** the follower counts are compared with the player's choice.
5. **Correct:** the screen is cleared, the score increases, B moves to A, a new B is drawn, and the game returns to step 2.
6. **Wrong:** the final score is shown and the game ends.
7. **Repeat or end:** the player types `ENTER` to clear the screen and play again, or anything else to quit.
Two Boolean flags control the loops. `another_round` keeps a single game going until the player guesses wrongly, and `playing` keeps the whole program running between games.
 
---
 
## Modular Code
 
The project is split across these files:
 
| File | Description |
|------|-------------|
| [`main.py`](main.py) | The game: its functions and the main game loop |
| [`art.py`](art.py) | The ASCII art logo and "VS" graphic |
| [`game_data.py`](game_data.py) | The data for 50 accounts, stored as a list of dictionaries |
| `index.html` | Runs the game in a web browser using Pyodide |
 
`index.html` also recognises a long run of blank lines, such as `print("\n" * 20)`, and clears the page instead of printing them. This makes the browser version behave like clearing the screen in a terminal.
 
Keeping the art and the data in their own files keeps `main.py` focused on the game's logic. It also means the list of accounts could be updated or extended without touching the game code.
 
---
 
## Reviewing and Debugging: My Process
 
Once my first version worked, I reviewed it carefully and tested how it behaved in unusual situations. I found four bugs and fixed them one at a time.
 
### Bug 1: The answer was shown on screen
 
While building the game, I added `print(followers)` so I could check that the follower counts were being stored correctly. I forgot to remove it, so the game displayed both follower counts before every guess. Deleting the line fixed it, and it taught me to check for leftover debugging code before finishing a project.
 
### Bug 2: The game could freeze
 
The program could pick the same account for both A and B. The two follower counts were then equal, so neither the "right" nor the "wrong" condition was true. The game redrew the same pair and asked again, and no answer could end the loop. With 50 accounts, this had a 1-in-50 chance of happening every time a new account was drawn.
 
I fixed this in two ways:
 
- I changed the comparisons from `>` to `>=`, so a tie counts as a correct answer whichever letter the player picks.
- I made sure the same account can't be drawn twice in a row (see Bug 4).
### Bug 3: Starting a new game compared the wrong numbers
 
The follower counts are stored in a list called `followers`. After a game ended, the last two counts were still in the list, and it was only cleared if the player typed exactly `ENTER`. If they typed anything else, the new game's counts were added after the old ones, but the program still compared the first two items. The player was being marked on the previous game's accounts.
 
I fixed this by clearing the list at the start of every game, whatever the player types:
 
```python
while playing:
    followers=[]
    showdown()
```
 
### Bug 4: A fix that caused a new bug
 
My first fix for duplicate accounts was to keep drawing until account B was different from account A:
 
```python
celebrity_2=select_celebrity()
while celebrity_1==celebrity_2:
    celebrity_2=select_celebrity()
```
 
This stopped duplicates appearing on screen, but `select_celebrity()` adds a follower count to the list every time it runs. When a duplicate was thrown away, its follower count stayed in the list. From then on, the list was one step behind the accounts on screen, and every comparison for the rest of the game used the wrong pair.
 
I fixed it by writing a separate function that removes the duplicate's follower count with `.pop()` before drawing again:
 
```python
def next_celebrity(first_celebrity):
    new_celebrity=select_celebrity()
    while new_celebrity==first_celebrity:
        followers.pop()
        new_celebrity=select_celebrity()
    return new_celebrity
```
 
Because the same check was needed in three places, putting it in one function also meant I only had to get it right once. This was the same lesson as my Day 11 Blackjack project: fixing one bug can create another, so the whole program needs re-testing after every change.
 
---
 
## Python Concepts Used
 
### 1. Lists of Dictionaries
 
Each account in `game_data.py` is a dictionary, and all 50 dictionaries are stored in a single list:
 
```python
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    ...
]
```
 
A value is looked up by its key, for example `celebrity['name']` or `celebrity['follower_count']`. Follower counts are stored in millions.
 
### 2. `random.choice()`
 
`random.choice()` picks a random item from a list, so it returns a whole account dictionary in one step:
 
```python
celebrity = random.choice(data)
```
 
My first version generated a random index with `random.randint(0, len(data) - 1)` and then looked up `data[location]`. `random.choice()` does the same job in fewer steps and is easier to read.
 
### 3. Importing Modules
 
The project uses two different styles of import:
 
```python
from game_data import data
import art
```
 
`from game_data import data` imports just the `data` list, so it can be used by name. `import art` imports the whole module, so its contents are accessed with a dot, as in `art.logo` and `art.vs`.
 
### 4. Nested Functions
 
`select_celebrity()`, `next_celebrity()` and `showdown()` are defined inside `game()`. This lets them all use the same `followers` list without passing it between them. Methods such as `.append()` and `.pop()` change the list in place, so every function sees the same, up-to-date list.
 
### 5. Working with Lists: `.append()`, `.pop()` and `del`
 
The `followers` list always holds the counts for the two accounts on screen:
 
- `.append()` adds the count for a newly drawn account to the end.
- `.pop()` removes the last count, which is used to discard a duplicate.
- `del followers[0]` removes account A's count after a correct guess, so B's count moves to the front.
### 6. Comparison Operators
 
The answer is checked by comparing the two counts. Using `>=` instead of `>` means a tie counts as correct:
 
```python
if choice=="A":
    if followers[0]>=followers[1]:
        print("That's right!")
```
 
### 7. `while` Loops and Boolean Flags
 
Two flags control the game's loops:
 
```python
playing=True          # keeps the program running between games
another_round=True    # keeps a single game going until a wrong guess
```
 
### 8. f-strings Across Multiple Lines
 
The display for each round is built from several f-strings. Python joins strings that sit next to each other inside brackets, so one `print()` can span several lines of code:
 
```python
print(f"{art.logo}\n"
f"Compare A: {celebrity_1}\n"
f"{art.vs}\n"
f"Against B: {celebrity_2}")
```
 
### 9. Clearing the Screen
 
After each correct guess, and before a new game, the screen is cleared by printing 20 new lines:
 
```python
print("\n" * 20)
```
 
Multiplying a string by a number repeats it, so `"\n" * 20` is 20 new lines. This pushes the previous round up the terminal, so the new round starts on a fresh section of the screen. In a very tall terminal window, part of the previous round may still be visible at the top. In the browser version, `index.html` clears the page completely. The screen isn't cleared after a wrong guess, so the player can still see the round they lost on.
 
### 10. Docstrings
 
Each function has a docstring, a short description in triple quotes that explains what it does:
 
```python
def select_celebrity():
    """Locates a celebrity within the data List, and assembles their data into a string"""
```
 
This was one of the improvements I listed in my Day 11 README, so I made sure to include it here.
 
---
 
## What I Learned
 
Key learning outcomes include:
 
- Storing structured data as a list of dictionaries and looking up values by key.
- Using `random.choice()` to pick an item directly from a list.
- Importing a whole module (`import art`) versus importing one name from it (`from game_data import data`).
- Defining functions inside another function so they can share the same list.
- Using `.append()`, `.pop()` and `del` to keep a list in step with what's on screen.
- Testing edge cases, such as ties and duplicate accounts, instead of only the normal path through the game.
- Resetting a game's data at the start of every game rather than relying on the player's input.
- Clearing the screen by printing a repeated string (`"\n" * 20`).
- Writing docstrings to explain what each function does.
- Removing debugging code before finishing a project.
The most important lesson was that storing the same information in two places is risky. The account names were in one variable and their follower counts were in a separate list, so every time I changed one, I had to remember to change the other. Two of my four bugs came from the two getting out of step.
 
---
 
## Future Improvements
 
- **Simplify the A and B branches:** the code for a correct or wrong guess is almost identical for `A` and `B`. Working out whether the guess is correct in a single line would remove the repetition:
```python
correct = (choice == "A" and followers[0] >= followers[1]) or (choice == "B" and followers[1] >= followers[0])
```
- **Ask again after invalid input:** a typo such as `C` currently ends the game. Asking the player again would be fairer.
- **Store the account dictionaries instead of a separate list:** keeping each account's dictionary, rather than a string plus a separate `followers` list, would keep the name and follower count together. The `.pop()` fix would then no longer be needed.
- **Use "a" or "an" correctly:** descriptions that start with a vowel are shown as "a Actress". The program could choose "an" when the description starts with a vowel.
- **Tidier play-again prompt:** adding `\n` to the end of the play-again question would put the player's answer on its own line.
- **Simpler play-again check:** typing `EXIT` and typing anything else now do the same thing, so the `elif again=="EXIT":` branch could be removed and left to `else`.
- **High score:** keep track of the best score across games in the same session.
---
 
## Course Context
 
This project was completed as part of Day 14 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.
 
Day 14 is the final project of the course's beginner section. Instead of introducing new concepts, it brings together everything from the first two weeks: lists, dictionaries, functions, loops, conditional statements, the `random` module and imported files. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.
 