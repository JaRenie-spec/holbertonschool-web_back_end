#!/usr/bin/env python3

"""
This module provides a function to calculate the length of
each element in an iterable of sequences.

The function `element_length` takes an iterable containing sequences
(such as strings, lists, etc.), and returns a list of tuples,
where each tuple contains a sequence and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of the input iterable
    and its corresponding length.

    This function takes an iterable of sequences (such as lists, strings, etc.)
    and returns a list of tuples. Each tuple consists of a sequence
    from the input iterable and the length of that sequence.

    Parameters:
        lst (Iterable[Sequence]):
        An iterable of sequences (e.g., list of strings or lists).

    Returns:
        List[Tuple[Sequence, int]]:
        A list of tuples, where each tuple contains a sequence
        from the input iterable and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
