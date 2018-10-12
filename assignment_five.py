
import random


def generate_pile():
    pile_number = random.randint(1, 10)
    return pile_number


def pick_pile():
    which_pile = float(input("Which pile?(1 or 2): "))
    while which_pile != 1 and which_pile != 2:
        print("The value you entered is not valid. Please try again.")
        which_pile = float(input("Which pile?(1 or 2): "))
    return which_pile


def how_many_stones():
    stones = float(input("How many stones?(1~3): "))
    while stones != 1 and stones != 2 and stones != 3:
        print("The value you entered is not valid. Please try again.")
        stones = float(input("How many stones?(1~3): "))
    return stones


def game():
    pile_1 = generate_pile()
    pile_2 = generate_pile()

    print("Pile 1: ", pile_1)
    print("Pile 2: ", pile_2)

    which_pile = pick_pile()
    stones = how_many_stones()
    if which_pile == 1:
        pile_1 = pile_1 - stones
    else:
        pile_2 = pile_2 - stones

    if pile_1 + pile_2 == 0:
        

    print("Pile 1: ", pile_1)
    print("Pile 2: ", pile_2)

