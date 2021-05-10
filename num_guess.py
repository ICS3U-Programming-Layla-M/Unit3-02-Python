#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May, 10, 2021
# This program asks the user to input a number between 0 and 9 and
# displays a message depending on if the guess is correct or wrong

import constants

# get the user guess
number = int(input("Guess what number I am thinking of between 0 and 9: "))


def main():
    # check if guess is correct and display message
    if (number == constants.CORRECT_GUESS):
        print("You guessed correctly!")

    # check if guess is incorrect and display message
    if (number != constants.CORRECT_GUESS):
        print("You guessed wrong")


if __name__ == "__main__":
    main()
