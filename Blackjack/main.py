import random
from Ascii_art import logo

player = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
cpu_cards = []


def give_card():
    card = random.choice(cards)
    return card


def calc_score(cards):
    if sum(cards)  == 21 and len(cards) == 2:
     return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def check(player_score, cpu_score):
    if player_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "You lose, opponent has Blackjack"
    elif player_score == 0:
        return "You won with a Blackjack"
    elif player_score > 21:
        return "You went over, You lose"
    elif cpu_score > 21:
        return "Opponent went over, You win"
    elif player_score > cpu_score:
        return "You win"
    else:
        return "You lose"


print(logo)


for i in range(2):
    player_cards.append(give_card())
    cpu_cards.append(give_card())

player_score = calc_score(player_cards)
cpu_score = calc_score(cpu_cards)

print(f"Your cards: {player_cards}, score: {player_score}")
print(f"Dealer's first card: {cpu_cards[0]}")

while player:
    if player_score == 0 or cpu_score == 0 or player_score > 21:
        player = False
    else:
        want_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if want_card == "y":
            player_cards.append(give_card())
            player_score = calc_score(player_cards)
            print(f"Your cards: {player_cards}, score: {player_score}")
        else:
            player = False

while cpu_score != 0 and cpu_score < 17:
    cpu_cards.append(give_card())
    cpu_score = calc_score(cpu_cards)


print(player_cards)
print(cpu_cards)

print(check(player_score, cpu_score))