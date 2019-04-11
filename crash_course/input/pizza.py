print("Please choose the topping for you\n")
print("(type 'quit' to exit)\n")
flag = True
number = 1

#adding only 3 toppings because the number < 4
while flag and number < 4:
    topping = input("Topping: ")
    if topping == 'quit':
        flag = False
    else:
        print("You added: " + topping)
        number += 1

    