"""
The simplest impossible math problem.
Introduction to collatz sequence.
"""


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


print("Please input integer to calculate the collatz sequence")
while True:
    try:
        number = int(input("Your starting number: "))
        print(number)
        while number != 1:
            number = collatz(number)
            print(number)
    except ValueError:
        print("Please use integer only")
