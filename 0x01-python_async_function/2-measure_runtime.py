#!/usr/bin/env python3
'''Measure runtime module.
'''
import asyncio
import time

from typing import List 

def measure_time(n: int, max_delay: int) -> float:
	'''
	run time computation
	'''
	start_time = time.time()
	asyncio.run(wait_n(n, max_delay))
	return (time.time() - start_time) / n