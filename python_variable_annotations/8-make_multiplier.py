from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by a specified multiplier.

    This function takes a float `multiplier` as an argument and returns a new function.
    The returned function takes a float `n` and multiplies it by the original `multiplier`.

    Parameters:
        multiplier (float): A float value that will be used to multiply the input number.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product
                                   of that float and the `multiplier` value.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
