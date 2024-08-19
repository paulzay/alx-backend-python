#!/usr/bin/env python3
"""function"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = (time.time() - start)/n
    return end
