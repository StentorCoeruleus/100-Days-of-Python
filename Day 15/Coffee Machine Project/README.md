# Coffee Machine: Python Vending Machine Simulator

## Overview

Coffee Machine is a text-based program I built in Python as the project for Day 15 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

It simulates a coffee vending machine. The user orders an espresso, latte or cappuccino, inserts coins to pay, and receives their drink and any change. The machine keeps track of its water, milk and coffee, refuses orders it doesn't have enough ingredients for, and stores the money it has taken. A hidden `report` command shows what's left, and `off` switches the machine off.

After my first version worked, I reviewed it, found several bugs, and fixed them one at a time. I also made the machine handle invalid input without crashing, and cleared the warnings my code editor was showing. This README describes the finished program and what I learned from that process.

---

## How to Use It

There are three ways to try the Coffee Machine.

### Option 1: Use it in your browser (no installation)

**[Launch the Coffee Machine](https://stentorcoeruleus.github.io/100-Days-of-Python/Day%2015/Coffee%20Machine%20Project/)**

This runs the Python code directly in your web browser using [Pyodide](https://pyodide.org/). Python takes a few seconds to load. Then type your answer into the box at the bottom of the black screen and press *Enter*. Type `off` to switch the machine off, then click **Restart coffee machine** to start again with a fully stocked machine.

For the best experience, use **Chrome** or **Edge**. Other browsers, such as Firefox and Safari, ask for your answers in pop-up boxes instead. Pressing **Cancel** in a pop-up switches the machine off.

### Option 2: Run it on your computer with Python 3

**Requirements**

- **Python 3.12 or newer**. You can download it from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"** during installation. (Some f-strings in this project use double quotes inside double quotes, which older versions of Python don't allow.)
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
cd "100-Days-of-Python/Day 15/Coffee Machine Project"
```
3. Run the Python script:
```bash
python main.py
```
   On macOS or Linux, you may need to type `python3 main.py` instead.
4. Type the name of a drink, then follow the on-screen prompts.

### Option 3: Run it in an online Python editor

The whole program is in one file, so it works in any online Python editor that uses Python 3.12 or newer, such as [Replit](https://replit.com/). Paste in the contents of `main.py` and click *Run*.

---

## The Menu

| Drink | Water | Milk | Coffee | Price |
|-------|-------|------|--------|-------|
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 100ml | 24g | $3.00 |

The machine starts with **300ml of water, 200ml of milk and 100g of coffee**, and $0.00.

It accepts four US coins:

| Coin | Value |
|------|-------|
| Quarter | $0.25 |
| Dime | $0.10 |
| Nickel | $0.05 |
| Penny | $0.01 |

---

## Commands

| Type | What happens |
|------|-------------|
| `espresso`, `latte` or `cappuccino` | Orders that drink |
| `report` | Shows the remaining water, milk and coffee, and the money taken |
| `off` | Switches the machine off |

Commands aren't case-sensitive, so `Latte` and `LATTE` also work. Anything else shows an error message and asks again.

---

## How the Program Works

### 1. Taking an Order

The machine asks what the user would like. If they type a drink on the menu, the order is processed. `report` and `off` are handled separately.

### 2. Checking the Resources

Before asking for any money, the machine checks that it has enough of every ingredient the drink needs. If something is running low, it names the ingredient, for example `Sorry, there is not enough water.`, and goes back to the start without taking anything.

### 3. Taking Payment

The user is asked how many quarters, dimes, nickels and pennies they're inserting, and the total is worked out.

- If an answer isn't a whole number, such as `ten` or `2.5`, or is negative, the machine explains the problem and asks for that coin again.
- **Not enough money:** the money is refunded and no drink is made.
- **Too much money:** the change is shown to two decimal places, for example `Here is $0.50 in change.`
- **Exact money:** the payment is accepted.

### 4. Making the Coffee

Only once the payment is accepted does the machine take the drink's price into its money total and deduct the ingredients from its resources. Then it serves the drink: `Here is your latte. Enjoy!`

### Example

```
What would you like? (espresso/latte/cappuccino)
latte
Please insert coins
How many quarters?
ten
You've typed an invalid value. Try typing a number such as '10'.
How many quarters?
12
How many dimes?
0
How many nickels?
0
How many pennies?
0
Here is $0.50 in change.
Here is your latte. Enjoy!
What would you like? (espresso/latte/cappuccino)
report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
What would you like? (espresso/latte/cappuccino)
cappuccino
Sorry, there is not enough water.
What would you like? (espresso/latte/cappuccino)
off
```

---

## Program Flow

1. **Ask:** the machine asks what the user would like.
2. **Report or off:** `report` prints the resources and returns to step 1; `off` ends the program.
3. **Invalid choice:** anything that isn't on the menu shows an error and returns to step 1.
4. **Check resources:** if any ingredient is short, the user is told which one, and the machine returns to step 1.
5. **Take payment:** the user enters their coins. If they haven't paid enough, the money is refunded and the machine returns to step 1.
6. **Make coffee:** the price is added to the machine's money, the ingredients are deducted, the drink is served, and the machine returns to step 1.

The Boolean flag `machine_on` keeps the main loop running until the user types `off`.

---

## Files

| File | Description |
|------|-------------|
| [`main.py`](main.py) | The whole program: the menu, resources, functions and main loop |
| `index.html` | Runs the program in a web browser using Pyodide |

`index.html` loads `main.py` directly, so the browser version always runs the latest version of the Python code. It replaces Python's `input()` with an input box inside the on-screen terminal, and Python pauses until the user presses *Enter*. In browsers that can't pause Python this way, it falls back to pop-up boxes.

---

## Functions

The program is split into five functions, each with one job:

| Function | What it does |
|----------|-------------|
| `check_resources(coffee)` | Returns `True` if there are enough ingredients for the drink, otherwise prints which one is short and returns `False` |
| `check_and_return_value(coin)` | Asks how many of one coin were inserted, and keeps asking until it gets a valid whole number |
| `check_money(coffee)` | Collects the coins, returns `True` if they cover the price (printing any change), otherwise refunds and returns `False` |
| `make_coffee(coffee)` | Takes the payment and deducts the drink's ingredients from the machine |
| `coffee_machine()` | Runs the main loop: taking orders, printing reports and switching off |

---

## Reviewing and Debugging: My Process

Once my first version worked, I tested it with unusual orders and inputs. I found several bugs and fixed them one at a time.

### Bug 1: Ordering an espresso crashed the program

My first version deducted water, milk and coffee for every drink. An espresso has no milk, so `MENU["espresso"]["ingredients"]["milk"]` doesn't exist, and Python stopped with a `KeyError`. I fixed this by only deducting milk for lattes and cappuccinos.

### Bug 2: Paying too much was rejected

My money check used the wrong comparison operator:

```python
if user_total > MENU[coffee]["cost"]:
    print("Sorry, that is not enough money.")
```

This rejected anyone who paid **more** than the price. Changing `>` to `<` fixed it.

### Bug 3: Ingredients were used up even when no drink was made

My first `check_resources()` deducted the ingredients first, then checked whether anything had dropped below zero. If the machine ran out of milk, the water and coffee had already been taken, even though no drink was made. Ingredients were also taken before the user paid.

I split this into two functions. `check_resources()` now only compares what the drink needs with what the machine has. `make_coffee()` deducts the ingredients, and it only runs after the payment has been accepted.

### Bug 4: A drink that used the last of an ingredient was refused

The old check used `<= 0`, so a drink that would leave exactly 0ml of water was refused. Comparing the amount needed with the amount available (`needed > available`) fixed this.

### Bug 5: The money total was replaced instead of added up

I stored each payment with `=`, so every sale overwrote the last one. After a latte ($2.50) and an espresso ($1.50), the report showed $1.50 instead of $4.00. Using `+=` fixed it. I also moved this line into `make_coffee()`, so money is only taken when a drink is actually made.

### Bug 6: The "not an option" message disappeared

While fixing the indentation of my final `else`, I moved it back one level too far, so it lined up with the `while` loop instead of the `if` statements:

```python
    while machine_on:
        ...
    else:
        print("Sorry, that was not an option. Please try again.")
```

Python has a feature called `while ... else`, where the `else` runs once when the loop's condition becomes `False`. My code didn't crash, but typing an invalid drink such as `mocha` no longer printed the error message. Indenting the `else` to line up with the `if` and `elif` statements fixed it.

### Bug 7: Typing a word instead of a number crashed the machine

The coin questions used `float(input(...))`. Typing `ten`, or pressing Enter without typing anything, made Python stop with a `ValueError`. I wrote a separate function that uses `try` and `except` to catch the error and ask again. It also rejects negative numbers and uses `int()` instead of `float()`, because you can't insert half a coin.

Because the same check was needed for all four coins, putting it in one function meant I only had to write it once.

### Understanding the Editor's Warnings

My code editor showed several yellow warnings that weren't errors, because the program still ran. Working out what they meant taught me how editors check types:

- **`'dict[str, int] | float'`:** each drink in `MENU` contains a dictionary (`"ingredients"`) and a float (`"cost"`). The editor couldn't tell which key gives which type, so it warned that `MENU[coffee]["ingredients"]` might be a float. I fixed this with a **type hint**: `MENU: dict[str, dict]`.
- **`'int | None'`:** my first coin function used `while True:` with a `return` inside the loop. The editor thought the loop could end without returning anything, giving `None`. I rewrote the loop to run `while number < 0`, with the `return` after it, so the function clearly always returns a whole number.

---

## Python Concepts Used

### 1. Nested Dictionaries

Each drink in `MENU` is a dictionary containing another dictionary for its ingredients. Values are reached by chaining keys:

```python
MENU["latte"]["ingredients"]["milk"]   # 150
MENU["latte"]["cost"]                  # 2.5
```

### 2. Checking Keys with `in`

`in` checks whether a key exists in a dictionary. It only checks the **top-level** keys, so it matches drink names but not `"cost"` or `"ingredients"`:

```python
elif opening in MENU:
```

This replaced a longer check (`opening == "espresso" or opening == "latte" or ...`), and any drink added to `MENU` would be accepted automatically.

### 3. Looping Through a Dictionary

A `for` loop over a dictionary gives its keys, which `check_resources()` uses to compare every ingredient a drink needs:

```python
for key in MENU[coffee]["ingredients"]:
    if MENU[coffee]["ingredients"][key] > resources[key]:
```

### 4. Functions That Return `True` or `False`

`check_resources()` and `check_money()` return a Boolean, so the main loop can decide what happens next:

```python
if enough_resources:
    enough_money = check_money(opening)
    if enough_money:
        make_coffee(opening)
```

`return` also ends a function straight away, which is how `check_resources()` stops at the first missing ingredient.

### 5. `try` and `except`

`try` runs some code, and if it causes a particular error, Python runs the `except` block instead of crashing:

```python
try:
    number = int(input(f"How many {coin}?\n"))
except ValueError:
    print("You've typed an invalid value. Try typing a number such as '10'.")
    continue
```

### 6. `continue`

`continue` skips the rest of the current pass through a loop and jumps back to the top. After an invalid answer, it sends the program straight back to ask the question again. It differs from `break`, which ends the loop completely, and `return`, which ends the whole function.

### 7. Input Validation Loops

`check_and_return_value()` starts `number` at `-1`, an invalid value, so the loop always runs at least once. It keeps asking until the answer is a whole number that isn't negative:

```python
number = -1
while number < 0:
    ...
return number
```

### 8. Formatting Money with `:.2f`

`round(x, 2)` rounds to *at most* two decimal places, but numbers don't keep trailing zeros, so `round(0.5, 2)` is still `0.5`. Adding `:.2f` inside an f-string always shows exactly two decimal places:

```python
print(f"Here is ${change:.2f} in change.")   # Here is $0.50 in change.
```

`round()` gives a number you can keep calculating with, while `:.2f` gives text for display.

### 9. Floating-Point Numbers

Computers store numbers in binary, so many decimals can't be stored exactly: `0.1 + 0.2` gives `0.30000000000000004`. This is why the coin total is rounded and money is displayed with `:.2f`. It's also why real payment systems often store money in whole pennies instead.

### 10. Type Hints

A type hint tells the code editor (and other developers) what type a variable should hold. It doesn't change how the program runs:

```python
MENU: dict[str, dict] = {
```

This says that `MENU`'s keys are strings and its values are dictionaries.

### 11. Augmented Assignment (`+=`)

`resources["money"] += MENU[coffee]["cost"]` is shorthand for `resources["money"] = resources["money"] + MENU[coffee]["cost"]`. It adds to the existing total instead of replacing it.

### 12. Docstrings

As in my Day 14 project, each function has a docstring explaining what it does. This time I made sure each one describes what the function **returns**, not just what it does.

---

## What I Learned

Key learning outcomes include:

- Storing data in nested dictionaries and reaching values by chaining keys.
- Using `in` to check a dictionary's keys, and understanding that it only checks the top level.
- Writing functions that return `True` or `False` so the main loop can decide what happens next.
- Catching errors with `try` and `except` so invalid input doesn't crash the program.
- Using `continue` to ask a question again, and how it differs from `break` and `return`.
- Displaying money with `:.2f`, and why `round()` alone isn't enough.
- Why floating-point numbers can't store most decimals exactly.
- Reading code-editor warnings and using type hints to make my intentions clear.
- That indentation can change what code means, as with `while ... else`.
- Giving each function one job, so it's easier to test and fix.

The most important lesson was **the order in which things happen matters**. Three of my bugs came from doing things too early: deducting ingredients before checking them, deducting them before payment, and taking money before the drink was made. Checking everything first, and only changing the machine's resources once the order is certain to succeed, fixed all three.

---

## Future Improvements

- **Store money in whole pennies:** using integers such as `250` instead of `2.50` would avoid floating-point rounding errors completely.
- **Loop through the ingredients in `make_coffee()`:** this would remove the hard-coded check for lattes and cappuccinos, so new drinks would work automatically:
```python
for item, amount in MENU[coffee]["ingredients"].items():
    resources[item] -= amount
```
- **Simplify `check_money()`:** the "too much" and "exact" branches both return `True`, so they could share that code, with only the change message added for overpayment.
- **Build the prompt from the menu:** `"/".join(MENU)` would list the drinks automatically, so a new drink would appear in the question too.
- **Add a `refill` command** to top the machine's resources back up.
- **Ignore extra spaces:** adding `.strip()` to the input would accept `latte ` with a trailing space.
- **Support older Python versions:** using single quotes inside f-strings, as in `{resources['water']}`, would let the program run on Python versions before 3.12.
- **Follow Python's style guide (PEP 8) more closely:** consistent spaces around `=` and comparison operators, capital letters for constants such as `QUARTER`, and a shorter function name such as `get_coin_count()`.

---

## Course Context

This project was completed as part of Day 15 of Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*.

Day 15 is the first day of the course's intermediate section. It introduces setting up a local development environment, and the project brings together dictionaries, functions with outputs, loops and conditional statements in a single program that has to keep track of its own state. The project forms part of my ongoing journey to develop my Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.