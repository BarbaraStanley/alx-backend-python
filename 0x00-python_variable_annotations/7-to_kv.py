#!/usr/bin/env python3

"""
A module that finds the square of a number in a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that returns a string and the square of v """
    square: Tuple[str, float] = (k, v**2)
    return square
