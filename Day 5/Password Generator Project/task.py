#the randomness is done without the use of shuffle() but using choosing random indexes in the list and removing that entry
#NOTE: to reduce complexity instead of using remove(), using pop() would be better:
# rand_index = secrets.randbelow(len(sublist))
# mixed.append(sublist.pop(rand_index))
import secrets

def mixed_list(parentlist: list[list[str]]):

    mixed_list=[]

    total_elements=sum(len(sublist) for sublist in parentlist)
    print(total_elements)
    non_empty_lists=[sublist for sublist in parentlist if len(sublist)>0]
    print("non empty lists: " + str(non_empty_lists))
    while total_elements > 0:
        sublist=secrets.choice(non_empty_lists)
        if len(sublist) > 0:
            selected_element=secrets.choice(sublist)
            sublist.remove(selected_element)
            print(non_empty_lists)
            mixed_list.append(selected_element)
            total_elements -= 1
        else:
            non_empty_lists.remove(sublist)
            print("non-empty_sublist after the removal of empty sublist: " + str(non_empty_lists))
            # l = [[i + j for j in range(100)] for i in range(0, 5000, 10)] --> tested the time reduction when deleting the empty sublists,
            # reduced from 284secs to 267secs

    print(mixed_list)
    password=""
    for char in mixed_list:
        password += char
    print(f"your password is: {password}")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

selected_letters= []
selected_numbers= []
selected_symbols= []

for i in range(nr_numbers):
    selected_numbers.append(secrets.choice(numbers))

for i in range(nr_symbols):
    selected_symbols.append(secrets.choice(symbols))

for i in range(nr_letters):
    selected_letters.append(secrets.choice(letters))


mixed_list([selected_numbers,selected_symbols,selected_letters])