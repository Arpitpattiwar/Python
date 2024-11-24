import Ascii_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
run = True

print(Ascii_art.logo)


def cipher(og_text, shift_num, direction):
    final = ""
    shift_num = shift_num % 26
    if direction == "decode":
        shift_num *= -1
    for letter in og_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            final += alphabet[(index + shift_num) % 26]
        else:
            final += letter
    if direction == "encode" or "decode":
        print(f"The {direction}d text is {final}.")
    else:
        print("Invalid input!!")


while run:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    direct = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    cipher(text, shift, direct)
    start = input("Do you want to continue? Yes or no!\n").lower()
    if start == "yes":
        run = True
    elif start == "no":
        run = False
    else:
        run = False
        print("INVALID OPTION\nBYE ")
