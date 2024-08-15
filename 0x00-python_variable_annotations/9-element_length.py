#!/usr/bin/env python3
"""element length"""

from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list of tuples"""
    return [(seq, len(seq)) for seq in lst]
