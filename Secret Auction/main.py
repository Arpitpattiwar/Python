import Ascii_art

print(Ascii_art.logo)
will_continue = True
bids = {}


def new_entry(name,bid):
    bids[name] = bid


while will_continue:
    new_name = input("Enter your name: ")
    person_bid=int(input("What is your bid: "))
    new_entry(new_name,person_bid)
    want_to_continue=input("Are there more bids?? Enter Yes or No: \n").lower()

    if want_to_continue != "yes":
        will_continue = False

max_bid = 0

for person in bids:
    if bids[person] > max_bid:
        max_bid = bids[person]
        max_name = person

print(f"\n{max_name} wins the auction with the highest bid of {max_bid}")