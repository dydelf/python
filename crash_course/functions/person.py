"""
finction which is returning a dictionary
"""

def build_person(first_name, last_name):
    """ return a dictionary information about the person """
    person = {'first_name': first_name, 'last_name': last_name}
    return person

MUSICIAN = build_person('david', 'bowie')
print(MUSICIAN)
