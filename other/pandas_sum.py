"""
Simple examples how to use pandas library.
"""

import pandas as pd

# reading the csv file
file = pd.read_csv('sitka_weather_07-2014.csv')

# printing the 5 headers of the file
print(file.head(5))


