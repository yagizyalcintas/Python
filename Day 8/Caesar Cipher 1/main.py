from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_length=len(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

#USING % IS BETTER SINCE YOU DONT NEED TO CHECK IF IT EXCEEDS THE ALP. SIZE AND NO NEED FOR SUBSTRACTION

def encrypt(original_text:str,shift_amount:int):
    encrypted=""
    for char in original_text:
        if alphabet.index(char)+shift_amount <= alphabet_length:
            encrypted += alphabet[alphabet.index(char)+shift_amount]
        else:
            encrypted += alphabet[alphabet.index(char)+shift_amount-alphabet_length]
    print(encrypted)

encrypt(text,shift)
