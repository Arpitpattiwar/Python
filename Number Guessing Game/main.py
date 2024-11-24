import random

play = True

def check(player_guess, ans):
    if ans == player_guess:
        print("You guessed it right!!")
    elif ans > player_guess:
        print("Too low")
    else:
        print("Too high")


while play:
    answer = random.randint(1, 101)

    level = input("Choose difficulty level. Type 'Easy' or 'Hard': ").lower()

    if level == "easy":
        chances = 10
    elif level == "hard":
        chances = 5
    else:
        print("Wrong input")
        chances = 0

    while chances > 0:
        guess= int(input("Make a Guess: "))

        if guess == answer:
            print("You guessed it")
            chances = 0
        elif answer > guess:
            chances -= 1
            print("Too low")
        else:
            chances -= 1
            print("Too high")

    play_again = input("Want to try again. 'y' or 'n': ").lower()

    if play_again != "y":
        play = False
