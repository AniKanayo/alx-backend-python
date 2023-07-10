#!/usr/bin/env python3

"""
This module demonstrates the task_wait_random function.
"""

import asyncio
from typing import Task
wait_random = __import__('3-tasks').wait_random

def task_wait_random(max_delay: int) -> Task:
    """
    Returns an asyncio.Task object for the wait_random coroutine with the specified max_delay.

    Args:
        max_delay: The maximum delay value.

    Returns:
        An asyncio.Task object representing the wait_random coroutine task.
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task

def main():
    """
    Main function to demonstrate the task_wait_random function.
    """
    max_delay = 5
    task = task_wait_random(max_delay)
    print(type(task))

if __name__ == "__main__":
    main()
