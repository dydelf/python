""" getting the largest palindrome from a list """

list_a = range(100, 999)
list_b = range(100, 999)

numbers = [a*b for a in list_a for b in list_b]
palindromes = []
for number in range(len(numbers)):
    if str(number) == ( str(number)[::-1]):
        palindromes.append(number)


print(palindromes)
