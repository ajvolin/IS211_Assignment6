#!/usr/bin/python
# -*- coding: utf-8 -*-

"""conversions.py: IS 211 Assignment 6."""

__author__ = 'Adam Volin'
__email__ = 'Adam.Volin56@spsmail.cuny.edu'

def convertCelsiusToKelvin(value):
    """ Converts Celsius to Kelvin.
    Parameters:
        value (float): the value to convert.
    
    Returns:
        (float): The converted value in Kelvin.
    
    Example:
        >>> convertCelsiusToKelvin(32)
        305.15
   """

    return round((float(value) + 273.15), 2)


def convertCelsiusToFahrenheit(value):
    """Converts Celsius to Fahrenheit.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Fahrenheit.

    Example:
        >>> convertCelsiusToFahrenheit(32)
        89.6
    """

    return round(((float(value) * 1.8) + 32), 2)


def convertFahrenheitToKelvin(value):
    """This function converts from Fahrenheit to Kelvin.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Kelvin.
    
    Example:
        >>> convertFahrenheitToKelvin(90)
        305.372
    """

    return round(((float(value) + 459.67) * 0.5555555556), 2)


def convertFahrenheitToCelsius(value):
    """This function converts from Fahrenheit to Celsius.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Celsius.

    Example:
        >>> convertFahrenheitToCelsius(90)
        32.22
    """

    return round(((float(value) - 32.0) * 0.5555555556), 2)


def convertKelvinToFahrenheit(value):
    """This function converts from Kelvin to Fahrenheit.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Fahrenheit.

    Example:
        >>> convertKelvinToFahrenheit(500)
        440.33
    """

    return round(((float(value) * 1.8) - 459.67), 2)


def convertKelvinToCelsius(value):
    """This function converts from Kelvin to Celsius.
    Parameters:
        value (float): the value to convert.

    Returns:
        (float): The converted value in Celsius.

    Example:
        >>> convertKelvinToCelsius(500)
        226.85
    """

    return round((float(value) - 273.15), 2)
