#!/usr/bin/env python3

"""
Module: 1-async_comprehension

    This module provides a coroutine for measuring the total runtime of
    executing async_comprehension four times in parallel.
"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    An asynchronous coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
