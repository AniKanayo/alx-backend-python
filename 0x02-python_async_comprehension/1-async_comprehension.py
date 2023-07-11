#!/usr/bin/env python3

"""
Module: 1-async_comprehension
    This module provides a coroutine for collecting 10 random numbers using
    an async comprehension
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous coroutine that collects 10 random numbers using an
    async comprehension

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    random_numbers = [number async for number in async_generator()][:10]
    return random_numbers
