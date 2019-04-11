"""
this is a module docstring, simple program to test the function
"""

def describe_city(city_country, city_name, city_people):
    """Display information about the city"""
    print("This " + city_name + " is in the country "
          + city_country + " and have " + city_people + " living inside ")

describe_city('Poland', 'Warszawa', '3000000')
#print("\n")
describe_city('Germany', 'Berlin', '4000000')
