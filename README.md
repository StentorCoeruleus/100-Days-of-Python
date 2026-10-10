# 100-Days-of-Python
My Projects from 100 Days of Code: The Complete Python Pro Bootcamp

# Treasure Island — Python Adventure Game

## Overview

Treasure Island is a text-based adventure game developed in Python as part of the final project of Day 3 of Dr Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

The game places the player on a quest to find hidden treasure on a mysterious island. Throughout the adventure, the player encounters a series of obstacles and must make decisions that determine how the story unfolds. Rather than using graphical environments or animated characters, the game runs entirely in the terminal. The player interacts with it by entering text-based choices, and the program responds to the decisions made. The objective of the game is to navigate the island successfully and find the treasure without falling into one of the traps along the way.

The game demonstrates how conditional logic can be used to create an interactive experience in which different choices lead to different outcomes.

## How the Game Works

The game follows a branching narrative structure. At each stage, the player is presented with a situation and must choose between the available options. The program evaluates the player's input and determines which part of the adventure should happen next. A correct decision allows the player to continue, while an incorrect decision leads to a game-over outcome.

### 1. Starting the Adventure

When the program starts, the player is introduced to the island and the objective of finding the treasure. The game uses text and ASCII art to establish the setting and create a simple visual representation of the adventure within the terminal.The player then begins making decisions that determine their route through the island.

### 2. Making Decisions

At each decision point, the player is presented with a choice. The options represent different actions the player can take to progress through the adventure. For example, for the first choice, the player would need to choose whether to turn left or right when the path splits into two. The program collects the player's response using Python's `input()` function. The response is then evaluated using conditional statements to determine the next stage of the game.

### 3. Following the Correct Path

The player's choices determine whether they can continue their journey.

If the player selects the correct option, the program moves them forward to the next challenge. For example, by turning left, the player progresses through the game and comes across the next obstacle. If they select an incorrect option, the player dies and receives a 'Game Ove,' ending the adventure. This branching structure means that the player's decisions, rather than random events, determine the outcome.

### 4. Winning or Losing

The adventure concludes when the player either reaches the treasure or encounters a fatal obstacle.

- Victory: The player makes the necessary decisions to reach the hidden treasure.
- Game over: The player makes a choice that leads to an unsuccessful outcome.

The game illustrates how a relatively small Python program can produce multiple possible outcomes through conditional logic.

##  Game Flow

The standard Treasure Island project follows this sequence:

1. Start:The player begins the treasure hunt.
2. First decision: The player chooses how to proceed through the initial obstacle.
3. Second decision: The player makes another choice to determine their route.
4. Final challenge: The player must make the correct decision to reach the treasure.
5. Outcome: The game displays either a winning message or a game-over message.

Each stage depends on the player's previous choice. The player must therefore follow the correct sequence of decisions to complete the adventure successfully.

## Python Concepts Used

This project introduces several fundamental Python programming concepts.

### 1. print() — Displaying Information

The print() function displays text in the terminal.

It is used to introduce the game, describe the player's surroundings, present choices, and communicate the consequences of each decision.

For example:
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

These statements provide the player with instructions and establish the objective of the game.

### 2. input() Function and Variables — Collecting Player Responses

The input() function pauses the program and waits for the player to enter a response.
E.g.,
trapdoor=input("Pick which door to enter. Type red, yellow, or blue.\n")

The information of the player's response is stored in a variable called 'trapdoor' that the program can use later. The program can then uses that value to decide what happens next. By combining variables, the input() function and conditional statements, the program becomes interactive rather than simply displaying a fixed sequence of messages.

### 3. Conditional Statements — 'if', 'elif' and 'else'

The Treasure Island game uses the principle of conditional statements to direct the player along different paths. Conditional statements allow the program to execute different blocks of code depending on whether particular conditions are met.
E.g.,
path=input("Do you go left or right? Type in your answer.\n").lower()
if path=="right":
    print("You have fallen into a ravine. Game Over.")
elif path=="left":
    print("You continue down the path and come to the edge of a large lake.")
    lake=input("Do you swim across or wait and build a raft? Type swim or wait.\n").lower() **(Adventure Continues)**
else:
    print("You continued past the path and fell into a ravine. Game Over.")

In this example, I have used multiple condition statement that the program compares the input value to to decide which indented statement to read. If the input value matches the requirements of the conditional statement, its indented code is read. For all values that fall outside the if or elif statement, the else statement is read. I used a third conditional statement for two choices to allow the gameplay to continue if the user entered a value that is not 'left' or 'right' and incorporated it into the choice of the gameplay, that is, them going past the path and having a 'Game Over.' I also made sure to use a .lower() function to account for the user entering different versions of 'left' or 'right' using uppercase characters (e.g., 'LEFT' or 'Right') by setting all characters to lowercase so that it can be read by the code. The result is a more seamless and polished code and gameplay. 

### 4. Nested Conditional Statements

A nested conditional is a conditional statement placed inside another conditional statement.

This allows the program to evaluate decisions in stages.

E.g.
path=input("Do you go left or right? Type in your answer.\n").lower()
if path=="right":
    print("You have fallen into a ravine. Game Over.")
elif path=="left":
    print("You continue down the path and come to the edge of a large lake.")
    lake=input("Do you swim across or wait and build a raft? Type swim or wait.\n").lower()
    if not lake=="wait":
        print("You decided to swim and were eaten alive by piranhas. Game Over.")
    else:
        print("You manage to get across the lake and enter a cave.\nThere are three trapdoors: red, yellow, and blue.")
        trapdoor=input("Pick which door to enter. Type red, yellow, or blue.\n")
else:
    print("You continued past the path and fell into a ravine. Game Over.")


In this example, the second decision is only evaluated if the player makes the correct first choice. Nested conditionals are useful for creating branching adventures because later decisions depend on earlier ones. Here, indentation is crucial to ensure that the correct sequence of responses occur to the correct inputs.

### 5. Logical Operators

Python's logical operators allow multiple conditions to be combined or evaluated together.

The two logical operators used are:

- 'or' logical operator — evaluates to `True` when at least one condition is true.
- 'not' logical operator — reverses a Boolean value.

Example 1:  trapdoor=input("Pick which door to enter. Type red, yellow, or blue.\n")
            elif trapdoor=="Yellow" or trapdoor=="yellow":
            print("You found King Midas' treasure. Congratulations, you win!")

Example 2: 
lake=input("Do you swim across or wait and build a raft? Type swim or wait.\n").lower()
    if not lake=="wait":
        print("You decided to swim and were eaten alive by piranhas. Game Over.")
    else:
        print("You manage to get across the lake and enter a cave.\nThere are three trapdoors: red, yellow, and blue.")

In the first example, the indented code is executed whether the user types 'yellow' or 'Yellow' which are both perceived as True. In the second example, if lake=="wait", it is read as False and the else conditional statement is executed instead.

Logical operators are useful for more complex decision-making, although a simple version of Treasure Island can be implemented primarily with `if`, `elif` and `else' statements.

### 6. ASCII Art

ASCII art uses ordinary text characters to create simple illustrations in the terminal. The game can use ASCII art to represent the island or introduce different scenes. Using a raw string, indicated by the `r` prefix, can make it easier to display text containing backslashes without Python treating them as escape sequences. ASCII art adds visual interest without requiring a graphics library or a graphical user interface.

## What I Learned

This project helped reinforce the fundamentals of Python programming by applying them to a small interactive game.

Key learning outcomes include:

- Using `print()` and `input()` to create a text-based user interaction.
- Storing user responses in variables.
- Using comparison operators to evaluate conditions.
- Controlling program execution with 'if', 'elif' and 'else' statements.
- Building branching logic with nested conditional statements.
- Understanding how logical operators combine Boolean conditions.
- Using indentation to define blocks of code.
- Displaying simple visual elements with ASCII art.
- Translating a sequence of rules and decisions into a working program.

The most important lesson is that  a program does not always need to execute from top to bottom in a single fixed sequence. Conditional statements allow it to respond differently depending on the information it receives.

## How to Run the Game

### Requirements

- Python 3 installed on your computer.
- A terminal, command prompt, or Python-compatible IDE.

No external libraries are required for the standard version of this project.

### Installation and Execution

1. Clone the repository or download the project files.
2. Open a terminal in the project directory.
3. Run the Python script.

Follow the on-screen prompts and enter your choices to play the game.

##  Future Improvements

Possible extensions to the project include:
- Replay functionality: Allow the player to restart the adventure after winning or losing.
- More branching paths: Introduce additional decisions, obstacles and endings.
- Inventory system: Allow the player to collect items and use them to overcome obstacles.
- Functions: Separate sections of the game into reusable functions to improve organisation.
- Random events: Introduce randomness to make different playthroughs less predictable.

These improvements could build on the existing program while providing opportunities to practise more advanced Python concepts.

## Course Context

This project was completed as part of **Day 3 of Dr Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

Day 3 focuses on conditional statements and control flow, with the Treasure Island project providing a practical application of decision-making in Python. The project forms part of my ongoing journey to develop Python programming skills, strengthen my understanding of software development fundamentals, and build a portfolio of practical coding projects on GitHub.
