from numpy.f2py.f90mod_rules import options

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
from collections import namedtuple
ops = [0,1,2]


def check_input(prompt: str, ops):
    print(ops)
    while True:
        try:
            inp = int(input(prompt + "\n"))
            if inp in ops:
                return inp
            else:
                print("invalid input, choose between 0,1,2")
        except ValueError:
            print("enter an integer")


def game_result(player_choice: int, comp_choice: int):
    if player_choice == comp_choice:
        print("its a draw!")
    elif ops[player_choice] == ops[comp_choice -1]:
        print("you lost!")
    else:
        print("you won!")




hand = namedtuple("hand", ["rock","paper","scissors"])
h = hand(rock,paper,scissors)
choice = check_input("choose 0 for rock, 1 for paper, 2 for scissors", ops)

comp_choice = random.choice(ops)
#print(choice)
#print(comp_choice)


print("your choice:\n")
print(h[choice] + "\n")
print("computer choice:\n")
print(h[comp_choice])


game_result(choice,comp_choice)

# if choice == 0:
#     print(h.rock +"\n")
#     print("computer choice:\n")
#     print()
#
