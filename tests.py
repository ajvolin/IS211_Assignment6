#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests.py: IS 211 Assignment 6."""

__author__ = 'Adam Volin'
__email__ = 'Adam.Volin56@spsmail.cuny.edu'

import unittest
import conversions as c
import conversions_refactored as cr


class ConversionsKnownValues(unittest.TestCase):
    """Tests conversion functions in conversions.py"""
    known_values = (
                        (0.00, 32.00, 273.15),
                        (32.00, 89.60, 305.15),
                        (48.00, 118.40, 321.15),
                        (100.00, 212.00, 373.15),
                        (-273.15, -459.67, 0.00),
                        (-373.15, -639.67, -100.00)
                    )


    def testConvertCelsiusToKelvin(self):
        """Tests that convertCelsiusToKelvin returns the expected value."""
        for val in self.known_values:
            from_val = val[0]
            expected_val = val[2]
            returned_val = c.convertCelsiusToKelvin(from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{}º Kelvin is not equal to expected value'
                                    ' of {}º Kelvin.') \
                                        .format(returned_val, expected_val)
                                )


    def testConvertCelsiusToFahrenheit(self):
        """Tests that convertCelsiusToFahrenheit returns the expected value."""
        for val in self.known_values:
            from_val = val[0]
            expected_val = val[1]
            returned_val = c.convertCelsiusToFahrenheit(from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{}º Fahrenheit is not equal to expected value'
                                    ' of {}º Fahrenheit.') \
                                        .format(returned_val, expected_val)
                                )


    def testConvertFahrenheitToKelvin(self):
        """Tests that convertFahrenheitToKelvin returns the expected value.""" 
        for val in self.known_values:
            from_val = val[1]
            expected_val = val[2]
            returned_val = c.convertFahrenheitToKelvin(from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{}º Kelvin is not equal to expected value'
                                    ' of {}º Kelvin.') \
                                        .format(returned_val, expected_val)
                                )


    def testConvertFahrenheitToCelsius(self):
        """Tests that convertFahrenheitToCelsius returns the expected value."""
        for val in self.known_values:
            from_val = val[1]
            expected_val = val[0]
            returned_val = c.convertFahrenheitToCelsius(from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{}º Celsius is not equal to expected value'
                                    ' of {}º Celsius.') \
                                        .format(returned_val, expected_val)
                                )
                                                 

    def testConvertKelvinToFahrenheit(self):
        """Tests that convertKelvinToFahrenheit returns the expected value."""
        for val in self.known_values:
            from_val = val[2]
            expected_val = val[1]
            returned_val = c.convertKelvinToFahrenheit(from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{}º Fahrenheit is not equal to expected value'
                                    ' of {}º Fahrenheit.') \
                                        .format(returned_val, expected_val)
                                )


    def testConvertKelvinToCelsius(self):
        """Tests that convertKelvinToCelsius returns the expected value."""
        for val in self.known_values:
            from_val = val[2]
            expected_val = val[0]
            returned_val = c.convertKelvinToCelsius(from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{}º Celsius is not equal to expected value'
                                    ' of {}º Celsius.') \
                                        .format(returned_val, expected_val)
                                )

class ConversionsRefactoredKnownValues(unittest.TestCase):
    """Tests convert function in conversions_refactored.py"""
    known_values = (
                        ('celsius', 'kelvin', 0.00, 273.15),
                        ('celsius', 'fahrenheit', 32.00, 89.60),
                        ('fahrenheit', 'kelvin', 118.40, 321.15),
                        ('fahrenheit', 'celsius', 212.00, 100.00),
                        ('kelvin', 'celsius', 0.00, -273.15),
                        ('kelvin', 'fahrenheit', -100.00, -639.67),
                        ('miles', 'yards', 1.00, 1760.00),
                        ('miles', 'feet', 2.00, 10560.00),
                        ('yards', 'miles', 6000.00, 3.41),
                        ('yards', 'feet', 120.00, 360.00),
                        ('feet', 'miles', 2640.00, 0.50),
                        ('feet', 'yards', 9000.00, 3000.00)
                    )


    def testConvert(self):
        """Tests that convert returns the expected value."""
        for val in self.known_values:
            from_unit = val[0]
            to_unit = val[1]
            from_val = val[2]
            expected_val = val[3]
            returned_val = cr.convert(from_unit, to_unit, from_val)
            self.assertEqual(returned_val,
                            expected_val,
                            msg=(
                                    '{} {} is not equal to expected value'
                                    ' of {} {}') \
                                        .format(returned_val, to_unit, expected_val, to_unit)
                                )
        

if __name__ == '__main__':
    unittest.main()
