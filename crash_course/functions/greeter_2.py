"""
making a greeter with input
"""

def get_formatted_name(first_name, last_name):
    """ Return a full name formatted """
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("press q to exit anytime")

    F_NAME = input("First name: ")
    if F_NAME == 'q':
        break
    L_NAME = input("Last name: ")
    if L_NAME == 'q':
        break

    print("\nHello " + get_formatted_name(F_NAME, L_NAME) + "!")
