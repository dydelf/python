#its possible to set one argument as a default with a = sign
def describe_pet(pet_type, pet_name):
    """Display information abou the pet"""
    print("I have a " + pet_type)
    print("My " + pet_type + "'s name is " + pet_name.title())

describe_pet('dog', 'burek')

describe_pet('cat', 'pyska')

#its possible to change the order with help of definition inside
describe_pet(pet_type = 'snake', pet_name = 'longie')

#when having one argument as a default,
#there is no need to specify it later