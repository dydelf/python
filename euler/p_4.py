"""
Euler problem 4
finding the largest palindrome
"""


def get_max_palindrome(numbers):
    """ getting the largest palindrome from a list """
    palindromes = []
    for number in range(len(numbers)):
        if str(number) == str(number)[::-1]:
            palindromes.append(number)
    max(palindromes)
    return max(palindromes)


# defining a list and getting palindrome
list_a = range(100, 999)
list_b = range(100, 999)

numbers = [a*b for a in list_a for b in list_b]
print(get_max_palindrome(numbers))

# defining a list of 2 digit multiplyiers and getting palindrome from it
list_c = range(1, 99)
list_d = range(1, 99)
numbers_2 = [c*d for c in list_c for d in list_d]
print(get_max_palindrome(numbers_2))

# checking if lists are correctly multiplied
list_aa = [1, 2, 3, 4, 5]
list_bb = [1, 2, 3, 4, 5]
numbers_ab = [aa*bb for aa in list_aa for bb in list_bb]
print(numbers_ab)

# euler program gives bad answer for 2 digit multipliers
# the same happens for a 3 digit ones
# logic of program correct
