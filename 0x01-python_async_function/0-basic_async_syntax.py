#!/usr/bin/env python3
'''
task 0 async
'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''random seconds
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

