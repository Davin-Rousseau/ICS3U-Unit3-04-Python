#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to input an integer
# and tells them if the integer is negative, positive, or 0


def main():
    # This function makes the user guess a number from 0-9

    # input
    numberInput = int(input("enter your number (integer): "))
    print("")

    # process
    if numberInput > 0:
        # output
        print("+")
    elif numberInput < 0:
        # output
        print("-")
    elif numberInput == 0:
        # output
        print("0")
    else:
        print("invalid")


if __name__ == "__main__":
    main()
