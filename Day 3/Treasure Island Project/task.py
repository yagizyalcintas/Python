
def input_check(prompt:str, options:list[str]):
    print(prompt)
    while True:

        answer = input()
        if answer in options:
            return answer
        else:
            print("the answer you provided is invalid, answer with a valid reply")

# input_check("left of right?", ["left", "right"])



print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


while True:

    decision = input_check("you are at a cross road, where do you want to go?\n Type left or right.\n", ["left","right"])

    if decision == "left":
        island = input_check("there is a lake with island in middle, wanna swim?\n type \"wait\" to wait a boat or \"swim\ to swim to island\n",["wait","swim"])
        if island == "swim":
            print("you got attacked by monster game over")
            break
        else:
            doorColor = input_check("you arrived unharmed, choose bw 3 doors, red, blue or yellow?\n",["yellow","blue","red"])
            if doorColor == "red":
                print("you got burned, game over")
                break
            elif doorColor == "blue":
                print("you got eaten by beasts, game over")
                break
            elif doorColor == "yellow":
                print("you won!")
                break

    elif decision == "right":
        print("you fell into a whole, game over")
        break
