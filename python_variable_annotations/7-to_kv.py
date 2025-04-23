from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a number.

    This function takes a string `k` and a number `v` (which can be an integer or a float),
    squares the number, and returns a tuple where the first element is the string `k`,
    and the second element is the square of `v` converted to a float.

    Parameters:
        k (str): A string value to be included in the tuple.
        v (Union[int, float]): A number (either integer or float) to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`, and the second
                           element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
