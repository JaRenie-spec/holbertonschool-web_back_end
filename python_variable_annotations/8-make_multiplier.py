#!/usr/bin/env python3

"""
This module provides a function that returns a multiplier function.

The `make_multiplier` function takes a multiplier as an argument
and returns a new function.
The returned function can be used to multiply
any given number by the original multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by a specified multiplier

    This function takes a float `multiplier` as an argument
    and returns a new function. The returned function takes a float `n`
    and multiplies it by the original `multiplier`.

    Parameters:
    multiplier (float): A float value that will be used
    to multiply the input number.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of that float and the `multiplier` value.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
