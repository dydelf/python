"""
Password manager.
"""

password = "haslo1234"

while password:

    user_input = input("What is your password? ")

    if password != user_input:
        print("This password is incorrect!")
    else:
        print("Access granted")
        break
