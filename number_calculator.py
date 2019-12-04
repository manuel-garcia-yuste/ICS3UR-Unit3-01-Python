#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program adds number


def main():
    # input
    number = float(input("Which is the first number: "))
    number1 = float(input("Which is the other number: "))

    # process
    answer = number + number1

    # output
    print("The answer is: " + str(round(answer, 2)))


if __name__ == "__main__":
    main()
