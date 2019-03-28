"""
Downloading data through API,
processing it and saving as a file ready for next steps
"""

import json
import pygal

filename = '/home/pyxis/python/project_population/data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


#for pop_dict in pop_data:
#    if pop_dict['Year'] == '2010':
#        country_name = pop_dict['Country Name']
#        population = pop_dict['Value']
#        print(country_name + ' ' + population)


# data sets for plotting
arab_pop = {}
euro_pop = {}
na_pop = {}
se_pop = {}
w_pop = {}


#extracting the data
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'Arab World':
        arab_year = pop_dict['Year']
        arab_population = int(float(pop_dict['Value']))
        arab_pop[arab_year] = arab_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'European Union':
        euro_year = pop_dict['Year']
        euro_population = int(float(pop_dict['Value']))
        euro_pop[euro_year] = euro_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'North America':
        na_year = pop_dict['Year']
        na_population = int(float(pop_dict['Value']))
        na_pop[na_year] = na_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'South Asia':
        se_year = pop_dict['Year']
        se_population = int(float(pop_dict['Value']))
        se_pop[se_year] = se_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'World':
        w_year = pop_dict['Year']
        w_population = int(float(pop_dict['Value']))
        w_pop[w_year] = w_population


print(arab_pop)
print(w_pop)
