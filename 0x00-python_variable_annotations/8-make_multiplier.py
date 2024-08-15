#!/usr/bin/env python3

"""function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ annotated function make_multiplier"""
    def multiply(number: float) -> float:
        """ annotated function make_multiplier"""
        return number * multiplier
    return multiply
