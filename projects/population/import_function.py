"""
Functions used for importing and extracting the specific sets of data
"""

import datapackage
import pandas as pd

"""package = Package('https://datahub.io/world-bank/sp.dyn.tfrt.in/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        resource.save('dataresource.json')
        #print(resource.read(keyed=True))
"""

data_url = 'https://datahub.io/world-bank/sp.dyn.tfrt.in/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])
        data.to_csv('data.csv')
