"""
Creating a simple class and using its instances as examples
"""


class Dog():
    """ A simple attempt to model a dog """

    def __init__(self, name, age):
        """ Initialize name and age attributes """
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate a dog sitting in response to a command """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ Simulate rolling over in response to a command """
        print(self.name.title() + " rolled over!")


# making an instance from a class
my_dog = Dog('willie', '12')

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# calling methods stored in a class Dog
my_dog.sit()
my_dog.roll_over()

# creating another instance from the same class
your_dog = Dog('jake', '3')
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()
