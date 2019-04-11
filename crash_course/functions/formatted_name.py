"""
this is a function for formatting name
"""
# defining normal function which i can use later in the program when given an arguments
def get_formatted_name(first_name, last_name):
    """ Return a full name, formatted """
    full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('David', 'Bowie'))
print(get_formatted_name('Pink', 'Floyd'))

# defining another function which uses one argument as a default one

def get_formatted_full_name(first_name, last_name, middle_name=''):
    """ Return a full name with middle name, formatted """
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

print(get_formatted_full_name('David', 'Bowie'))
print(get_formatted_full_name('Pink', 'Floyd'))

# combining the two functions

def get_formatted_name_combined(first_name, last_name, middle_name=''):
    """ return a full name with or without a middle name """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name_combined('David', 'Bowie', 'Starman'))
print(get_formatted_name_combined('Pink', 'Floyd'))
print(get_formatted_name_combined('Freddie', 'Mercury', 'Queen'))
