#!/usr/bin/env python3

"""
This module demonstrates the wait_n async routine.
"""

import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> float:
    """
    Async routine that spawns wait_random n times with the specified max_delay.
    Returns a list of delays (float values) in ascending order.
    """
    await asyncio.sleep(max_delay)
    return uniform(0, max_delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay.
    Returns a list of delays (float values) in ascending order.
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    delays = sorted(delays)
    return delays
