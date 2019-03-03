#creating dictionary with lists of the cities

cities = {
    'berlin': {
        'country': 'germany',
        'population': '100',
        'fact': 'good city',
    },
    'paris': {
        'country': 'france',
        'population': '200',
        'fact': 'muslims',
    },
    'london': {
        'country': 'england',
        'population': '300',
        'fact': 'polish people',
    },
}

for city, city_info in cities.items():
    print(city + ": is in the country - " + city_info['country'])
