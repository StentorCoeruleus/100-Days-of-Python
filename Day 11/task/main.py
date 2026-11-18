import random
import art

def random_card():
    return random.choice(cards)


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

game_running=True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while game_running:

    my_cards = []
    my_score=0

    computer_cards = []
    computer_score=0

    dealing_cards=True
    computer_turn=True

    game_start=input("Would you like to play a game of Blackjack?\n"
    "Type 'ENTER' to start, or 'EXIT' to quit.\n").upper()

    if game_start == "ENTER":
        print("\n" * 100)
        print(art.logo)

        for deal in range(2):
            my_cards.append(random_card())
            computer_cards.append(random_card())

        my_score=calculate_score(my_cards)
        computer_score=calculate_score(computer_cards)

        print(f"My cards: {my_cards}, current score: {my_score}\n"
        f"Computer's first card: {computer_cards[0]}")

        if computer_score==0 or my_score==0:
            dealing_cards=False
            computer_turn=False

        while dealing_cards:
            another_card=input("Type 'HIT' to get another card, or 'STAND' to pass.\n").upper()
            if another_card == "HIT":
                my_cards.append(random_card())
                my_score=calculate_score(my_cards)
                if my_score == 21:
                    dealing_cards = False
                elif my_score>21:
                    dealing_cards = False
                    computer_turn = False
                else:
                    print(f"My cards: {my_cards}, current score: {my_score}\n"
                    f"Computer's first card: {computer_cards[0]}")
            elif another_card == "STAND":
                dealing_cards = False
            else:
                print("Sorry, that's not an option. Try again.")

        if computer_turn:
            while computer_score<17:
                computer_cards.append(random_card())
                computer_score=calculate_score(computer_cards)


        print(f"Your final hand: {my_cards}, final score: {my_score}\n"
              f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        showdown(computer_score,my_score)

    elif game_start == "EXIT":
        game_running = False
    else:
        print("Sorry, that's not an option. Restarting game...")


