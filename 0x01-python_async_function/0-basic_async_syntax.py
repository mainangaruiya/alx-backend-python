#!/usr/bin/env python3
# countasync.py

import asyncio
import random

async def wait_random(max_delay=10):
	delay = random.uniform(0, max_delay) 
	await asyncio.sleep(delay)
	return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
