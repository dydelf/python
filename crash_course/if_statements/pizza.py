requested_toppings = ['mushrooms', 'pepperoni', 'cheese', 'bacon']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'cheese':
            print("Sorry, no " + requested_topping + " today!")
        else:
            print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

