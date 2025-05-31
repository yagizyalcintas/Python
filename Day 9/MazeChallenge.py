
#refer to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_left():
    pass
def wall_in_front():
    pass
def wall_on_right():
    pass
def move():
    pass
def at_goal():
    pass
def front_is_clear():
    pass


# Notes:
# 1-if left, right and forward is occupied, should turn back
# 2-if two side if occupied, should go to the remaining direction
# 3- if more than 1 direction is possible, choose randomly
# 4-there should be a better way to do step 3, using memory.
import random


def wall_on_left():
    turn_left()
    if front_is_clear():
        turn_right()
        return False
    else:
        turn_right()
        return True


def directions_freeness_status():
    front = True
    right = True
    left = True
    if wall_in_front():
        front = False
    if wall_on_right():
        right = False
    if wall_on_left():
        left = False
    return {"left": left, "right": right, "front": front}


def choose_direction():
    dirs = directions_freeness_status()
    print("dirs: " + str(dirs))
    available_directions = []
    for dir, is_open in dirs.items():
        if is_open:
            available_directions.append(dir)
    print("open directions are: " + str(available_directions))
    if available_directions:
        decision = available_directions[random.randint(0, len(available_directions) - 1)]
    else:
        decision = "back"
    return decision


def turn_right():
    for i in range(0, 3):
        turn_left()


def reach_goal():
    while not at_goal():
        next_step = choose_direction()
        if next_step == "front":
            move()
        elif next_step == "back":
            turn_left()
            turn_left()
            move()
        elif next_step == "left":
            turn_left()
            move()
        elif next_step == "right":
            turn_right()
            move()


reach_goal()