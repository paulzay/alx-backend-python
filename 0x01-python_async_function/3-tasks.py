#!/usr/bin/env python3
"""function"""


def task_wait_random():
    """docs"""
    import asyncio
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random())
