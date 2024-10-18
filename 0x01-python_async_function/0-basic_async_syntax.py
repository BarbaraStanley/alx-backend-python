#!/usr/bin/env python3

"""
A module that generates a random float
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A coroutine that generates a float between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)  # Wait for the random delay
    return delay
