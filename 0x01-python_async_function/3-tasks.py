#!/usr/bin/env python3

"""
This module demonstrates the task_wait_random function.
"""
import asyncio
from asyncio.tasks import Task
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Returns an asyncio.Task object for the wait_random coroutine with the
    specified max_delay.

    Args:
        max_delay: The maximum delay value.

    Returns:
        An asyncio.Task object representing the wait_random coroutine task.
    """
    def wait_random():
        async def inner_wait_random():
            await asyncio.sleep(max_delay)
            return

        loop = asyncio.get_event_loop()
        task = loop.create_task(inner_wait_random())
        return task

    return wait_random()
#    loop = asyncio.get_event_loop()
#    task = loop.create_task(wait_random(max_delay))
#    return task
