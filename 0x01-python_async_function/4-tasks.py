#!/usr/bin/env python3

"""
This module demonstrates the task_wait_random function.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns an asyncio.Task object for the wait_random coroutine with the specified max_delay.
    """
    coroutines = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
