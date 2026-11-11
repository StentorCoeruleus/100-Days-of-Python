import random
import hangman_words
import hangman_art

print(hangman_art.logo)
print("Welcome to the Hangman Game!")
lives = 6

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guesses = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in guesses:
        print(f"You have already guessed {guess}. Please try again.")
    guesses.append(guess)
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
                display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\nThe word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
