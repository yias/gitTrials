#!/usr/bin/env python
"""
    developer: Iason Batzianoulis
    maintaner: Iason Batzianoulis
    
"""


import numpy as np


def fun(a, b):
    print( np.sum( np.array([a, b]) ) )

def fre(c, d):
    print(np.ones( [c, d]) )

fun(1, 3)
fun(4, 5)
fun(5, 6)
