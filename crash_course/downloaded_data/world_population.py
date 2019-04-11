"""
Working on json data file and visualizing data hidden inside
"""

import json
import pygal
from country_codes import get_country_code

# load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
# build a dictionary with population data
cc_populatons = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populatons[code] = population

# group the countries by 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populatons.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# see how many countries are on each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

mm = pygal.maps.world.World()
mm.title = 'World population by country in 2010'
mm.add('0-10mln', cc_pops_1)
mm.add('10mln-1bln', cc_pops_2)
mm.add('>1bln', cc_pops_3)

mm.render_to_file('world_population.svg')
