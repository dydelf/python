"""
formatting a name with a function for the purpose of testing the code
"""

from name_function import get_formatted_name

print("press q to exit anytime")
while True:
    first = input("Write your first name: ")
    if first == 'q':
        break
    last = input("Write your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\nNeatly formatted name: " + formatted_name)
