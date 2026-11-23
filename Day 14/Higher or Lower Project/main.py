import random
from game_data import data
import art

def game():
    """Contains the code encompassing the 'Higher or Lower' game"""

    followers=[]
    playing=True


    def select_celebrity():
        """Locates a celebrity within the data List, and assembles their data into a string"""
        celebrity = random.choice(data)
        followers.append(celebrity['follower_count'])
        return f"{celebrity['name']}, a {celebrity['description']} from {celebrity['country']}"

    def next_celebrity(first_celebrity):
        """Selects a new celebrity for celebrity_2, but first checks if the celebrity chosen is the same as celebrity_1.
         If so, a new celebrity is chosen, and the follower count of the last celebrity is deleted from the followers List"""
        new_celebrity=select_celebrity()
        while new_celebrity==first_celebrity:
            followers.pop()
            new_celebrity=select_celebrity()
        return new_celebrity

    def showdown():
        """Compares celebrity_1 and celebrity_2 and determines if the guess by the user is correct."""
        celebrity_1=select_celebrity()
        celebrity_2=next_celebrity(celebrity_1)
        score=0
        another_round=True
        while another_round:
            print(f"{art.logo}\n"
            f"Compare A: {celebrity_1}\n"
            f"{art.vs}\n"
            f"Against B: {celebrity_2}")
            choice=input("Who has more followers? Type 'A' or 'B':\n").upper()

            if choice=="A":
                if followers[0]>=followers[1]:
                    print("\n" * 20)
                    print("That's right!")
                    score+=1
                    print(f"Current score: {score}")
                    del followers[0]
                    celebrity_1=celebrity_2
                    celebrity_2=next_celebrity(celebrity_1)
                elif followers[1]>followers[0]:
                    print("Sorry, that's wrong.")
                    print(f"Final score: {score}")
                    another_round = False
            elif choice=="B":
                if followers[1]>=followers[0]:
                    print("\n" * 20)
                    print("That's right!")
                    score+=1
                    print(f"Current score: {score}")
                    del followers[0]
                    celebrity_1 = celebrity_2
                    celebrity_2 = next_celebrity(celebrity_1)
                elif followers[0]>followers[1]:
                    print("Sorry, that's wrong.")
                    print(f"Final score: {score}")
                    another_round=False
            else:
                print("Sorry, that's wrong.")
                print(f"Final score: {score}")
                another_round = False

    while playing:
        followers=[]
        showdown()
        again=input("Would you like to play again? Type 'ENTER' to start or 'EXIT' to quit.").upper()
        if again=="ENTER":
            print("\n" * 20)
        elif again=="EXIT":
            playing=False
        else:
            playing=False


game()









