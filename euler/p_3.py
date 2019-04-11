"""
Euler problem 3
Finding the largest prime factor of a given number
"""

def get_dividers(number):
    """ Getting the dividers of a given number """
    dividers = []
    for i in range(1, number+1):
        if(number % i == 0):
            dividers.append(i)
    return dividers

def get_primals(numbers):
    """ taking primes from the given list """
    primals = []
    for number in numbers:
        isPrime = True
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                isPrime = False
                break
        if isPrime:
            primals.append(number)
    return primals


dividers = [get_dividers(600851475143)]
print(get_dividers(600851475143))

