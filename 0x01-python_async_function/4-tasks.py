#!/usr/bin/env python3
"""comment"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n():
    """comment"""
    return asyncio.create_task(wait_n(5, 10))
