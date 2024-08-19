#!/usr/bin/env python3
"""function"""

import time


def measure_time():
    """function"""
    start = time.time()
    yield
    end = time.time()
    return end - start
