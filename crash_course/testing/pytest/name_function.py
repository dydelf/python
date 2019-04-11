"""
function of formating a name for the purpose of testing
"""


def get_formatted_name(first, last, middle=''):
    """ Generate a neatly formatted name """
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
