"""
Downloading data through API,
processing it and saving as a file ready for next steps
"""

import json
#import matplotlib
#matplotlib.use('tkagg')
#from matplotlib import pyplot as plt
#import seaborn as sns
#import pandas as pd
import pygal

filename = 'data/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ' ' + population)


# data sets for plotting
arab_pop = {}
euro_pop = {}
na_pop = {}
se_pop = {}
la_pop = {}
a_pop = {}

w_pop = {}


#extracting the data
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'Middle East & North Africa (all income levels)':
        arab_year = int(float(pop_dict['Year']))
        arab_population = int(float(pop_dict['Value']))
        arab_pop[arab_year] = arab_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'Europe & Central Asia (all income levels)':
        euro_year = int(float(pop_dict['Year']))
        euro_population = int(float(pop_dict['Value']))
        euro_pop[euro_year] = euro_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'North America':
        na_year = int(float(pop_dict['Year']))
        na_population = int(float(pop_dict['Value']))
        na_pop[na_year] = na_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'East Asia & Pacific (all income levels)':
        se_year = int(float(pop_dict['Year']))
        se_population = int(float(pop_dict['Value']))
        se_pop[se_year] = se_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'Latin America & Caribbean (all income levels)':
        la_year = int(float(pop_dict['Year']))
        la_population = int(float(pop_dict['Value']))
        la_pop[la_year] = la_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'Sub-Saharan Africa (all income levels)':
        a_year = int(float(pop_dict['Year']))
        a_population = int(float(pop_dict['Value']))
        a_pop[a_year] = a_population
for pop_dict in pop_data:
    if pop_dict['Country Name'] == 'World':
        w_year = int(float(pop_dict['Year']))
        w_population = int(float(pop_dict['Value']))
        w_pop[w_year] = w_population



visual = pygal.Line()

visual.title = "Population during last years in regions of the World"
visual.x_title = "Year"
visual.y_title = "Population"
visual.x_labels = [i for i in range(1960, 2010)]
visual.add('Middle East & North Africa', arab_pop)
visual.add('Europe & Central Asia', euro_pop)
visual.add('North America', na_pop)
visual.add('East Asia & Pacific', se_pop)
visual.add('Latin America & Caribbean', la_pop)
visual.add('Sub-Saharan Africa', a_pop)

visual.render_to_file('population.svg')

#df_arab = pd.DataFrame(arab_pop, index=[0])
#sns.set_style("darkgrid")
#arab_visual = sns.lineplot(data=df_arab, dashes=False)
#plt.show()
