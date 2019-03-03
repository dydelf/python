from random import randint
print("Would you like to roll a dice? ")
active = True
while active:
    print("This is your number: " + str(randint(1,6)))
    again = input("Again? ")
    if again == 'no':
        active = False