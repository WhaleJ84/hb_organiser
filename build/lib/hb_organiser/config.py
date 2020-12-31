"""
Contains the values for flags to prevent having to specify them via CLI
"""
from os.path import abspath


class Config:
    """
    Contains the values for flags to prevent having to specify them via CLI
    """
    PROJECT_ROOT = abspath('../')
    SOURCE = ''
    DESTINATION = ''
