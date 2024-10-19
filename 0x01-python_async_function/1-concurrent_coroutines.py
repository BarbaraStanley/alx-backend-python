#!/usr/bin/env python3

"""
A module 
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A coroutine that generates a float between 0 and max_delay"""
    wait = []
    td = [wait_random(max_delay) for _ in range(n)]
    
    for i in asyncio.as_completed(td):
        delay = await i
        wait.append(delay)
    
    return wait
