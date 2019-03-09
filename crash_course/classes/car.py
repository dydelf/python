"""
Creating a car class and
modyfying instances and arguments with different functions
"""


class Car():
    """ a simple attempt to represent a car """

    def __init__(self, make, model, year):
        """ initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ return a neatly formatted name """
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """ reading and printing odometer """
        msg = "This car's mileage is: "
        msg += str(self.odometer_reading) + " miles"
        return msg

    def update_odometer(self, mileage):
        """ update odometer reading,
            reject change if value is lesser than 0 or lower than previous one
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't turn back the odometer!")
        return

    def increment_odometer(self, miles):
        """ add additional miles to the odometer """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Incorrect value!")
        return

"""
# getting basic information about the car
my_new_car = Car('audi', 'a3', '1992')
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

# trying different combinations of updating the odometer
my_new_car.update_odometer(20)
print(my_new_car.read_odometer())

my_new_car.update_odometer(-10)
print(my_new_car.read_odometer())

# incrementing the odometer and testing
my_new_car.increment_odometer(10)
print(my_new_car.read_odometer())

my_new_car.increment_odometer(-10)
print(my_new_car.read_odometer())
"""
