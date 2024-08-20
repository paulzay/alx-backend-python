#!/usr/bin/env python3
"""async comprehension"""

import time
import asyncio

start_time = time.time()

async_comprenhension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """docs"""
    await asyncio.gather(*(async_comprenhension() for i in range(4)))
    return time.time() - start_time
