#!/usr/bin/env python3

"""
Module: 0-async_generator
This module provides an async generator coroutine for generating
random floating-point numbers.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields random floating-point numbers
    between 0 and 10.
    Returns:
        AsyncGenerator[float, None]:An async generator that produces random
        floating-point numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
