#!/usr/bin/env python3

"""
A module that adds lists
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ A function that returns the sum of a list of int and floats """
    return sum(mxd_lst)
