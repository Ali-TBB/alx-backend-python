#!/usr/bin/env python3
"""Sum a mixed list of floats and integers"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Sum a mixed list of floats and integers"""
    return sum(mxd_lst)
