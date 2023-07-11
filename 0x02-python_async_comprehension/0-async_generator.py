#!/usr/bin/env python3

"""
Module
"""
import asyncio
import random


async def async_generator():
    numbers = []
    for _ in range(10):
        """ Function """
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
