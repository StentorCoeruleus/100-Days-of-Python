print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("\nYou have arrived at the island of Nyxos.You are in a thick forest amidst heavy fog.\nHowever, you notice that the path has split into two.")
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
        if trapdoor=="red" or trapdoor=="Red":
            print("You entered a furnace and were burned alive. Game Over.")
        elif trapdoor=="Yellow" or trapdoor=="yellow":
            print("You found King Midas' treasure. Congratulations, you win!")
        elif trapdoor=="blue" or trapdoor=="Blue":
            print("You find an angry grizzly bear disturbed from hibernation and were eaten alive. Game Over.")
        else:
            print("You took too long to decide and the cave collapsed on top of you in an earthquake. Game Over.")
else:
    print("You continued past the path and fell into a ravine. Game Over.")




