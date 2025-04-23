from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all elements in a list of integers and floats and returns the result.

    This function takes a list that can contain both integers and floats, calculates
    the total sum of the elements in the list, and returns the sum as a float.

    Parameters:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats to be summed.

    Returns:
        float: The sum of all elements in the input list, returned as a float.
    """
    return sum(mxd_lst)
