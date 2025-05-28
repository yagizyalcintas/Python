print(10 % 3)

try:
    userInput= int(input("give a number\n"))
    if (userInput%2) == 0:
        print("userInput is even")
    else:
        print("user input is odd")
except ValueError:
    print("you did not enter a number type")