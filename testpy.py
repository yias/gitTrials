#!/usr/bin/env python
"""
    developer: Iason Batzianoulis
    maintaner: Iason Batzianoulis
    email: iason.batzianoulis@ansys.com
    description:
    process of creating a VM and then deleting it
"""


import numpy as np


def fun(a, b):
    print( np.sum( np.array([a, b]) ) )

fun(1, 3)
fun(4, 5)
fun(5, 6)