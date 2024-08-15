#!/usr/bin/env python3

"""function"""


def make_multiplier(multiplier: float) -> callable:
    """return multiplier"""
    def multiplier(n: float) -> float:
        """return float of n"""
        return n * multiplier
    return multiplier
