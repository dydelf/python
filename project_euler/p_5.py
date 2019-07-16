"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

def evenly_divided(a, b):
    """Function finding smallest number evenly divided in range (a, b)."""
    number = [range(1, 10000)]
    for i in number:
        div = [range(a, b)]
        for x in div:
            divisors = []
            if int(i) % int(x) == 0:
                divisors.append(x)
            if len(divisors) == len(a, b):
                return i


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def evenly_divided_2(num):
    """Function finding smallest number evenly divided in range (a, b)."""
    number = list(range(1, 10000))
    for i in number:
        divisors = []
        for x in num:
            if int(i) % int(x) == 0:
                divisors.append(x)
        return divisors

print(evenly_divided_2(num))
