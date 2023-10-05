#!/usr/bin/env python3
'''
float and int
'''
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return float(sum(mxd_lst))
