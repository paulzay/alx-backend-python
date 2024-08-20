#!/usr/bin/env python3
"""4 tas"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """wait n"""
    delays = []
    for i in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delays)]
