"""A module for demonstrating exceptions"""

import sys

def convert(s):
    '''convert to a integer'''
    try:
        return int(s)
    except (ValueError, TypeError):
        raise