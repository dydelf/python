"""
simple testing method usung pytest
"""

import pytest
from name_function import get_formatted_name


def test_first_last_name():
    """ Do names look like Janis Joplin? """
    assert get_formatted_name('janis', 'joplin') == 'Janis Joplin'


def test_first_last_middle_name():
    """ Do names look like Wolfgang Amadeus mozart? """
    assert get_formatted_name('wolfgang', 'mozart', 'amadeus') == 'Wolfgang Amadeus Mozart'
