#!/usr/bin/env python3
"""Multiply two numbers"""


def make_multiplier(multiplier: float) -> callable:
    """Return a function that multiplies a number by multiplier"""
    def f(n: float) -> float:
        return n * multiplier
    return f

