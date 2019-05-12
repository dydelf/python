"""
Degree converter from Celsius to Fahrenheit.
"""

def convert_to_fahrenheit(c):
    if c < -273.15:
        return "There can't be such a low temperature!"
    else:
        f = c * (9/5) + 32
        return f

c = float(input("What is the number of degrees that you want to convert? "))
print("The value in Fahrenheit is: " + str(convert_to_fahrenheit(c)) 
        + " degrees.")
