"""
Creating a car class and inheritance
modyfying instances and arguments with different functions
creating inheritance of car class - electric car
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
        print("This car's mileage is: " +
              str(self.odometer_reading) + " miles")

    def update_odometer(self, mileage):
        """ update odometer reading,
            reject change if value is lesser than 0 or lower than previous one
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't turn back the odometer!")

    def increment_odometer(self, miles):
        """ add additional miles to the odometer """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Incorrect value!")


class ElectricCar(Car):
    """ represent aspects of a car but an electric one """
    def __init__(self, make, model, year):
        """ initialize attributes of the parent class """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """ describe the battery inside the car """
        print("This car has a " + str(self.battery_size) + " kWh battery")

    def get_range(self):
        """ print statement about the range of the battery """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


# getting basic information about the car
my_tesla = ElectricCar('tesla', 'model S', '2017')
print(my_tesla.get_descriptive_name())
print(my_tesla.read_odometer())

# trying different combinations of updating the odometer
my_tesla.update_odometer(20)
print(my_tesla.read_odometer())

my_tesla.update_odometer(-10)
print(my_tesla.read_odometer())

# incrementing the odometer and testing
my_tesla.increment_odometer(10)
print(my_tesla.read_odometer())

my_tesla.increment_odometer(-10)
print(my_tesla.read_odometer())

print(my_tesla.describe_battery())
print(my_tesla.get_range())
