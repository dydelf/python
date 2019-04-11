"""
working with a csv file and visualizing data inside it
"""

import csv
from datetime import datetime
import matplotlib
matplotlib.use('tkagg')
from matplotlib import pyplot as plt

# opening a file and reading the first row inside it
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # printing the headers one by one
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # get dates and high temperatures from the file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', linewidth='1', alpha=0.5)
plt.plot(dates, lows, c='blue', linewidth='1', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title("Daily high and low temperatures - 2014", fontsize=16)
plt.xlabel('', fontsize=10)
# draws the date label diagonally
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=6)
plt.tick_params(axis='both', which='major', labelsize=6)


plt.show()
