print("Welcome to the rollercoaster!")


while True:

    try:
        height = int(input("whats your height?"))
        break
    except ValueError:
        print("the height is wrong type")

if height >= 180:
    print("you can ride")
else:
    print("you cant ride")