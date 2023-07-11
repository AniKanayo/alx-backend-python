#!/usr/bin/env python3

"""
This module demonstrates the wait_n async routine.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay.
    Returns a list of delays (float values) in ascending order.
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    delays = sorted(delays)  # Sorting the delays in ascending order
    return delays
