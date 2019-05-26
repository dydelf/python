"""
main core of the program,
this is the place where everything is going to be plotted together
"""

import json
import pygal
import timing


filename = 'data/population_estimates.json'
with open(filename) as f:
    pop_data = json.load(f)


for pop_dict in pop_data:
    if pop_dict['Year'] == '2015':
        print(pop_dict['Region'] + ' - ' + pop_dict['Population'])


# data sets for plotting
africa_pop = {}
europe_pop = {}
na_pop = {}
asia_pop = {}
la_pop = {}
oceania_pop = {}

world_pop = {}


#extracting the data
for pop_dict in pop_data:
    if pop_dict['Region'] == 'AFRICA':
        africa_year = int(float(pop_dict['Year']))
        africa_population = int(float(pop_dict['Population']))
        africa_pop[africa_year] = africa_population
for pop_dict in pop_data:
    if pop_dict['Region'] == 'EUROPE':
        europe_year = int(float(pop_dict['Year']))
        europe_population = int(float(pop_dict['Population']))
        europe_pop[europe_year] = europe_population
for pop_dict in pop_data:
    if pop_dict['Region'] == 'NORTHERN AMERICA':
        na_year = int(float(pop_dict['Year']))
        na_population = int(float(pop_dict['Population']))
        na_pop[na_year] = na_population
for pop_dict in pop_data:
    if pop_dict['Region'] == 'ASIA':
        asia_year = int(float(pop_dict['Year']))
        asia_population = int(float(pop_dict['Population']))
        asia_pop[asia_year] = asia_population
for pop_dict in pop_data:
    if pop_dict['Region'] == 'LATIN AMERICA AND THE CARIBBEAN':
        la_year = int(float(pop_dict['Year']))
        la_population = int(float(pop_dict['Population']))
        la_pop[la_year] = la_population
for pop_dict in pop_data:
    if pop_dict['Region'] == 'OCEANIA':
        oceania_year = int(float(pop_dict['Year']))
        oceania_population = int(float(pop_dict['Population']))
        oceania_pop[oceania_year] = oceania_population
for pop_dict in pop_data:
    if pop_dict['Region'] == 'WORLD':
        world_year = int(float(pop_dict['Year']))
        world_population = int(float(pop_dict['Population']))
        world_pop[world_year] = world_population



visual = pygal.Line()

visual.title = "Population during last years in regions of the World"
visual.x_title = "Year"
visual.y_title = "Population"
visual.x_labels = [i for i in range(1950, 2015)]
visual.add('Africa', africa_pop)
visual.add('Europe', europe_pop)
visual.add('Northern America', na_pop)
visual.add('Asia', asia_pop)
visual.add('Latin America & Caribbean', la_pop)
visual.add('Oceania', oceania_pop)

visual.render_to_file('population.svg')
