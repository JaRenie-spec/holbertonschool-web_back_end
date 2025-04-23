#!/usr/bin/env python3

"""
This module provides a function to calculate the floor value of a given floating-point number.

It uses the math.floor() function to return the largest integer less than or equal to the input number.
"""

import math

def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the given float.

    This function uses the math.floor() method to return the floor of the input float.

    Parameters:
        n (float): The number for which the floor value is to be calculated.

    Returns:
        int: The largest integer less than or equal to the input float.
    """
    return math.floor(n)
