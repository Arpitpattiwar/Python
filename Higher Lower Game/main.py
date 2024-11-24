import os
import random

import art
import data

play = True
print(art.logo)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check(listA, listB):
    """Will return if the guess is correct"""
    if listA['follower_count']  > listB['follower_count']:
        ans = "a"
    else:
        ans = "b"

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess != ans:
        return 0
    elif ans == "a":
        return listA
    else:
        return listB


while play:
    correct_guess = True
    score = 0

    A = random.choice(data.data)
    B = random.choice(data.data)
    while A == B:
        B = random.choice(data.data)

    while correct_guess:
        print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
        print(art.vs)
        print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}")

        result = check(A, B)

        if result == 0:
            correct_guess = False
        else:
            score += 1
            print(f"Score: {score}")
            A = result
            B = random.choice(data.data)
            while A == B:
                B = random.choice(data.data)

    print(f"You scored {score}")

    want_to_play = input("Type 'y' to play again, 'n' to exit: ").lower()
    if want_to_play == 'n':
        play = False
    else:
        clear_screen()


