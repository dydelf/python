"""
Euler problem 3
Finding the largest prime factor of a given number
"""

def get_primals(number):
    """ Getting the prime factors of given number """
    """  [i for i in number % == 0] """
    dividers = []
    for i in range(1, number+1):
        if(number % i == 0):
            dividers.append(i)
    primals = []
    for divider in dividers:
        isPrime = True
        for num in range(2, divider):
            if divider % num == 0:
                isPrime = False
        if isPrime:
            primals.append(divider)
    return primals

print("primals of the number 600851475143 are: " +
      str(get_primals(600851475143)))
print(max(get_primals(600851475143)))
