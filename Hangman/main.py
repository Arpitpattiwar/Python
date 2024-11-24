import os
import random
import Ascii, word_list

display = []
game_over = False
chosen_word = random.choice(word_list.word_list)
print(chosen_word)
lives = 6

for pos in range(len(chosen_word)):
    display += "_"

print(Ascii.logo + "\n")
while not game_over:
    print(Ascii.stages[lives])
    guess = input("Guess a letter: ").lower()
    if guess in display:
        os.system('cls')
        print(Ascii.logo + "\n")
        print(display)
        print(f"You've already guessed {guess}")
    else:
        for pos in range(len(chosen_word)):
            if chosen_word[pos] == guess:
                display[pos] = guess
        print(Ascii.logo + "\n")

        print(display)
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print(Ascii.stages[lives])
                print("You lose!!! ")
                print("The word was " + chosen_word)
        print(f"You have {lives} lives left")

    guess_exist = False

    if "_" not in display:
        game_over = True
        print("You win")