"""
Visual representation of one set of die rolling.
"""

from die import Die
import pygal

# create a D6
die = Die()

# make rolls and store it in the list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyze the results counting each number repetition
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results with a histogram
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency od the result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
