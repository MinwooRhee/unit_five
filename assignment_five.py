# Minwoo Rhee
# 10/16/18
# assignment_five
# a game of guessing a random number from 1 to 100

import random


def instruction():
    """
    give instructions of the program
    :return: None
    """
    print("Welcome to the game of guessing!")
    print("Computer will pick a random number between 1 - 100 and you are going to guess the number.")
    print("With every guess, Computer will tell you if the guess was too high or too low.")


def game():
    """
    game is all in this function
    :return: None
    """
    number = random.randint(1, 100)
    how_many_guesses = 0  # add 1 to this variable every time player guesses

    while True:
        guess = int(input("Pick a number between 1 and 100: "))
        if guess > 100 or guess < 1:
            print("Please enter a valid number.")
        elif guess > number:
            print("Your guess is too high.")
            how_many_guesses = how_many_guesses + 1
        elif guess < number:
            print("Your guess is too low.")
            how_many_guesses = how_many_guesses + 1
        else:
            how_many_guesses = how_many_guesses + 1
            print("Congratulations! You got it in", how_many_guesses, "guesses.")
            break


def main():
    instruction()

    while True:
        print(" ")  # blank line to increase readability
        y_or_n = input("Would you like to guess my number?(y/n) ")

        if y_or_n == "y":
            game()
        elif y_or_n == "n":
            print("Good bye!")
            break
        else:
            print("Please enter a valid answer.")


main()
