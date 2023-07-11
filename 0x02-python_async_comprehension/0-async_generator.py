#!/usr/bin/env python3

"""
Module
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    for _ in range(10):
        """ Function """
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
