"""
greeting users from a list
"""

def greet_users(names):
    """ greet users from a list """
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)

USERS = ['maciek', 'flora', 'alicja']
greet_users(USERS)
