"""
Visual representation of the two sets of die rolling.
"""

from die import Die
import pygal

# create a two D6 dice
die_1 = Die(20)
die_2 = Die(20)

# make rolls and store it in the list
results = [die_1.roll() + die_2.roll() for roll_num in range(100000)]
#for roll_num in range(10000):
#    result = die_1.roll() + die_2.roll()
#    results.append(result)

# analyze the results counting each number repetition
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
#for value in range(2, max_result+1):
#    frequency = results.count(value)
#    frequencies.append(frequency)

# visualize the results with a histogram
hist = pygal.Bar()

hist.title = "Results of rolling two D6 10000 times"
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
x_labels = [i for i in range(2, max_result+1)]
#for i in range(0, len(x_labels)):
#    x_labels[i] = str(x_labels[i])
hist.x_labels = [str(i) for i in x_labels]
# another way for conversion is
# test_list = list(map(int, test_list))
hist.x_title = "Result"
hist.y_title = "Frequency od the result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
