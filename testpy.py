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


if __name__ == "__main__":
    fun(1,3)