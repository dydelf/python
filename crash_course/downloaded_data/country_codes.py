"""
getting a country code in pygal
"""

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """ getting a 2 letter country code """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the country wasn't found, return none
    return None
