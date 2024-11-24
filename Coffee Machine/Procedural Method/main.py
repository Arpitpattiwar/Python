from Ingredients import MENU, resources

milk = resources['milk']
coffee = resources['coffee']
water = resources['water']


def order(item, w, m, c):
    order_details = MENU[item]['ingredients']
    insufficient_ingredients = ""
    ii_count = 0

    if water > order_details['water'] and milk > order_details['milk'] and coffee > order_details['coffee']:
        w -= order_details['water']
        m -= order_details['milk']
        c -= order_details['coffee']
        return w, m, c, "Enjoy your drink!!"
    else:
        if water < order_details['water']:
            insufficient_ingredients = "water"
            ii_count += 1
        if milk < order_details['milk']:
            if ii_count > 0:
                insufficient_ingredients += " and "
            insufficient_ingredients += "milk"
        if coffee < order_details['coffee']:
            if ii_count > 0:
                insufficient_ingredients += " and "
            insufficient_ingredients += "coffee"
        return w, m, c, f"Sorry there is not enough {insufficient_ingredients}."


def report():
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}")


def refill(w, m, c):
    w += int(input("How much water do you want to fill: "))
    m += int(input("How much milk do you want to fill: "))
    c += int(input("How much coffee do you want to fill: "))
    return w, m, c


while 2 > 1:
    order_item = input("What would you like(Espresso, Latte, Cappuccino): ").lower()

    if order_item == "report":
        report()
    elif order_item == "refill":
        water, milk, coffee = refill(water, milk, coffee)
    elif order_item in MENU:
        print("Insert money")
        ten_note = int(input("Rs 10 notes: "))
        twenty_notes = int(input("Rs 20 notes: "))
        fifty_notes = int(input("Rs 50 notes: "))
        hundred_notes = int(input("Rs 100 notes: "))

        amount_received = 10 * ten_note + 20 * twenty_notes + 50 * fifty_notes +100 * hundred_notes

        if MENU[order_item]['cost'] > amount_received:
            print("Sorry that's not enough money. Money refunded")
        else:
            water, milk, coffee, machine_response = order(order_item, water, milk, coffee)
            print(machine_response)
            if MENU[order_item]['cost'] < amount_received and machine_response == "Enjoy your drink":
                print(f"Here is your change: {amount_received - MENU[order_item]['cost']}")

