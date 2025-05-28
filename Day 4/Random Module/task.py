import random

def coin_toss():
    result = random.random()
    print(result)
    if result > 0.5:
        print("Heads")
    else:
        print("Tails")


coin_toss()