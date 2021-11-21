#"Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs...Loop until the user chooses not to perform any more calculations."
from typing import MutableMapping


def calculate():
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    done = False
    while not done:
        operation = input("(a)dd, (s)ubtract, (m)ultiply, or (d)ivide?")
        if operation == "a":
            print(num1 + num2)
        elif operation == "s":
            print(num1 - num2)
        elif operation == "m":
            print(num1 * num2)
        elif operation == "d":
            print(num1 // num2)
        done = True


calculate()


#Exercise 2:
def pyramid(n):
    for level in range(n):
        print(" " * (n - level - 1) + "X" * (2 * level + 1))

(pyramid(4))
