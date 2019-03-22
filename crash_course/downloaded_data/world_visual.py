"""
Working on json data file and visualizing world population over the years
"""

import json
import matplotlib
matplotlib.use('tkagg')
from matplotlib import pyplot as plt

# load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
# build a dictionary with world  population data
world_population = {}
years, pop = [], []
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'World':
        year = int(pop_dict['Year'])
        population = int(float(pop_dict['Value']))
        world_population[year] = population
        years.append(year)
        pop.append(population)

# plotting a visual using a dictionary
#plt.plot(range(len(world_population)), world_population.values())
#plt.xticks(range(len(world_population)), list(world_population.keys()))

# converting keys of dictionary into the values
print(years)
year_keys = list(world_population.keys())
print(year_keys)
print(world_population)

# plotting a visual graph
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(years, pop, c='blue', linewidth='5')
#plt.hist(years, pop)

# formatting plot
plt.title("World population in recent years")
plt.xlabel('Years', fontsize=9)
plt.ylabel('Population', fontsize=9)
plt.tick_params(axis='both', which='major', labelsize=6)

plt.show()
