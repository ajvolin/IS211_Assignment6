#!/usr/bin/python
# -*- coding: utf-8 -*-

"""conversions_refactored.py: IS 211 Assignment 6."""

__author__ = 'Adam Volin'
__email__ = 'Adam.Volin56@spsmail.cuny.edu'

class UnitDoesNotExistException(Exception):
    pass

class ConversionNotPossibleException(Exception):
    pass

def convert(from_unit, to_unit, value):
    """This function converts from unit to another.
    Parameters:
        from_unit (str): the unit to convert from.
        to_unit (str): the unit to convert to.
        value (float): the value to convert.

    Returns:
        (float): The converted value.

    Examples:
        >>> convert('celsius', 'kelvin', 32)
        305.15
        >>> convert('kelvin', 'fahrenheit', 500)
        440.33
        >>> convert('miles', 'feet', 1)
        5280.0
    """
    
    # Unit conversion dictionary, uses lambdas to complete the conversions
    unit_conversions = {
        'celsius': {
            'kelvin': lambda x: round((float(x) + 273.15), 2),
            'fahrenheit': lambda x: round(((float(x) * 1.8) + 32), 2)
        },
        'fahrenheit': {
            'kelvin': lambda x: round(((float(x) + 459.67) * 0.5555555556), 2),
            'celsius': lambda x: round(((float(x) - 32.0) * 0.5555555556), 2)
        },
        'kelvin': {
            'fahrenheit': lambda x: round(((float(x) * 1.8) - 459.67), 2),
            'celsius': lambda x: round((float(x) - 273.15), 2)
        },
        'miles': {
            'yards': lambda x: round((float(x) * 1760), 2),
            'meters': lambda x: round((float(x) * 1609.344), 2),
            'feet': lambda x: round((float(x) * 5280), 2)
        },
        'yards': {
            'miles': lambda x: round((float(x) / 1760), 2),
            'meters': lambda x: round((float(x) / 1.094), 2),
            'feet': lambda x: round((float(x) * 3), 2)
        },
        'meters': {
            'miles': lambda x: round((float(x) / 1609.344), 2),
            'yards': lambda x: round((float(x) * 1.094), 2),
            'feet': lambda x: round((float(x) * 3.281), 2)
        },
        'feet': {
            'miles': lambda x: round((float(x) / 5280), 2),
            'yards': lambda x: round((float(x) / 3), 2),
            'meters': lambda x: round((float(x) / 3.281), 2)
        }
    }

    # Convert units to lowercase to match unit_conversions dict keys.
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # Check if from_unit exists as a key in unit_conversions dict.
    if from_unit in unit_conversions:
        # Check if from_unit is the same as to_unit, if so just return value as float.
        if from_unit == to_unit:
            return float(value)
        # Check if to_unit exists as a key in unit_conversions[from_unit] dict, if so pass value to lambda.
        elif to_unit in unit_conversions[from_unit]:
            return unit_conversions[from_unit][to_unit](value)
        # Raise ConversionNotPossibleException if to_unit does not exist as a key in unit_conversions[from_unit] dict.
        else:
            raise ConversionNotPossibleException
    # Raise UnitDoesNotExistException if from_unit does not exist as a key in unit_conversions dict.
    else:
        raise UnitDoesNotExistException
