# TODO-1: Import and print the logo from art.py when the program starts.
from sympy.codegen.ast import continue_

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
#  TODO-3: Can you figure out a way to restart the cipher program?



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")





def decrypt(original_text, shift_amount):
    shift_amount = shift_amount % len(alphabet)
    print("shift_amount: " + str(shift_amount))
    decrypted=""
    for letter in original_text:
        if letter not in alphabet:
            decrypted += letter
        else:
            decrypted += alphabet[alphabet.index(letter)-shift_amount]

    print(decrypted)

def restartPrompt():
    res = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
    if res == "yes":
        ceasar()
    elif res == "no":
        pass
    else:
        print("enter a valid option")
        restartPrompt()

def ceasar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("enter an integer")
    if direction=="encode":
        encrypt(original_text=text, shift_amount=shift)
        restartPrompt()
    elif direction=="decode":
        decrypt(original_text=text,shift_amount=shift)
        restartPrompt()
    else:
        print("choose a valid option")
        ceasar()

ceasar()

