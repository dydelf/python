"""
Calculate the length of a string.
"""

def length_of_string(s):
    if type(s) == int:
        return "Integers doesn't have any length"
    else:
        return "The length is: " + str(len(s))

s = input("Enter any string: ")
print(length_of_string(s))
