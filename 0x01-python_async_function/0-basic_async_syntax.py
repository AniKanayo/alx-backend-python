#!/usr/bin/env python3
"""
Module:
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds (inclusive). Returns the generated delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# async def main():
#    """
#    Main function to demonstrate the wait_random coroutine.
#    """
#    delays = []
#    for _ in range(3):
#        delay = await wait_random()
#        delays.append(delay)
#        print(delay)

# asyncio.run(main())
