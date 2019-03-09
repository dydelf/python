"""
working with a classes by importing them
"""

from car import Car

# getting basic information about the car
my_new_car = Car('audi', 'a3', '1992')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(50)
print(my_new_car.read_odometer())



