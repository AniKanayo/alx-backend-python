#!/usr/bin/env python3

"""
This module demonstrates the task_wait_random function.
"""

import asyncio
from typing import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Returns an asyncio.Task object for the wait_random coroutine with the specified max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task


def main():
    """
    Main function to demonstrate the task_wait_random function.
    """
    max_delay = 5
    tasks = [task_wait_random(max_delay) for _ in range(5)]
    delays = asyncio.run(asyncio.gather(*tasks))
    print(delays)

if __name__ == "__main__":
    main()
