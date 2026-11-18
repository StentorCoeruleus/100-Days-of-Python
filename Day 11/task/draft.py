import random
import art

game_running=True

while game_running:

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = []
    my_score = 0

    computer_cards = []
    computer_score = 0

    dealing_cards = True

    game_start = input("Do you want to play a game of Blackjack? Type 'ENTER' to start or 'EXIT' to quit.\n").upper()

    if game_start == "ENTER":
        print("\n" * 100)
        print(art.logo)
        for shuffle in range(0,2):
            my_chosen_card=random.choice(cards)
            my_cards.append(my_chosen_card)
            my_score+=my_chosen_card
            computer_chosen_card=random.choice(cards)
            computer_cards.append(computer_chosen_card)
            computer_score+=computer_chosen_card

        print(f"your cards: {my_cards}, current score: {my_score}\n"
              f"computer's first card: {computer_cards[0]}")

        if computer_score > 21:
            print("Ace Detected!")
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_score -= 10
            print(f"your cards: {my_cards}, current score: {my_score}\n"
                  f"computer's first card: {computer_cards[0]}")

        if my_score > 21:
            my_cards.remove(11)
            my_cards.append(1)
            my_score -= 10
            print(f"your cards: {my_cards}, current score: {my_score}\n"
                  f"computer's first card: {computer_cards[0]}")

        if computer_score==21 or my_score==21:
            dealing_cards=False


        while dealing_cards:
            another_card = input("Type 'HIT' to take another card, or type 'STAND' to pass.\n").upper()

            if another_card == "HIT":
                my_chosen_card = random.choice(cards)
                my_cards.append(my_chosen_card)
                my_score += my_chosen_card

                if my_score > 21 and 11 in my_cards:
                        print("Ace Detected!")
                        my_cards.remove(11)
                        my_cards.append(1)
                        my_score -= 11
                        my_score += 1

                if my_score >= 21:
                    dealing_cards = False
                else:
                    print(f"your cards: {my_cards}, current score: {my_score}\n"
                      f"computer's first card: {computer_cards[0]}")


            elif another_card == "STAND":
                dealing_cards = False

        while not computer_score >= 17:
            computer_chosen_card = random.choice(cards)
            computer_cards.append(computer_chosen_card)
            computer_score += computer_chosen_card
            if computer_score>21:
                if 11 in computer_cards:
                    print("Ace Detected!")
                    computer_cards.remove(11)
                    computer_cards.append(1)
                    computer_score -= 11
                    computer_score += 1

        print(f"Your final hand: {my_cards}, final score: {my_score}\n"
          f"Computer's final hand: {computer_cards}, final score: {computer_score}")


        if computer_score == 21 and my_score==21 and len(my_cards)==2 and len(computer_cards)==2:
            print("It's a draw!")
        elif computer_score == 21 and len(computer_cards)==2:
            print("Computer has Blackjack! You lose!")
        elif my_score==21 and len(my_cards)==2:
            print("You have Blackjack! You win!")
        elif my_score > 21:
            print("Bust! You lose!")
        elif computer_score>21:
            print("You win!")
        elif my_score == computer_score:
            print("It's a draw!")
        elif computer_score>my_score:
                print("You lose!")
        elif my_score>computer_score:
                print("You win!")

    elif game_start == "EXIT":
        game_running=False
    else:
        print("Sorry, that is not an option. Restarting game...")






