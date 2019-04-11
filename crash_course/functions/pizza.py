"""
printing an arbitrary number of pizza toppings from a list
"""

def printing_toppings(*toppings):
    """ using arbitrary number of arguments """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

#printing many toppings using just one function
printing_toppings('pepperoni')
printing_toppings('cheese', 'crust', 'pepperoni', 'mushrooms')


#arbitrary argument needs to be the last one on the arguments list

#for adding additional arguments after the basic ones add an argument with **
# example (first_name, last_name, **other_user_info)
#this can create a dictionary with as many arguments as I would like
