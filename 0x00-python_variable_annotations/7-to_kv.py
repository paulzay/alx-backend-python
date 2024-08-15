#!/usr/bin/env python3

"""function"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string k and an int OR float v as arguments,"""
    return (k, float(v**2))
