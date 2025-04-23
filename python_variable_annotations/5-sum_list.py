from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums all the elements in a list of floats and returns the result.

    This function takes a list of floats and calculates the total sum of the elements
    in the list, returning the sum as a float.

    Parameters:
        input_list (List[float]): A list of float numbers to be summed.

    Returns:
        float: The sum of all the elements in the input list.
    """
    return sum(input_list)
