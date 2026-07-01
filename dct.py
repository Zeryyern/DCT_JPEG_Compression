"""
dct.py
Manual implementation of Forward and Inverse DCT
"""

import numpy as np
import math


# JPEG normalization coefficient
def C(k):
    return 1 / math.sqrt(2) if k == 0 else 1


# Forward Discrete Cosine Transform
def dct_2d(block):

    dct = np.zeros((8, 8))

    for u in range(8):
        for v in range(8):

            total = 0

            for x in range(8):
                for y in range(8):

                    total += (
                        block[x][y]
                        * math.cos(((2 * x + 1) * u * math.pi) / 16)
                        * math.cos(((2 * y + 1) * v * math.pi) / 16)
                    )

            dct[u][v] = 0.25 * C(u) * C(v) * total

    return dct


# Inverse Discrete Cosine Transform
def idct_2d(block):

    image = np.zeros((8, 8))

    for x in range(8):
        for y in range(8):

            total = 0

            for u in range(8):
                for v in range(8):

                    total += (
                        C(u)
                        * C(v)
                        * block[u][v]
                        * math.cos(((2 * x + 1) * u * math.pi) / 16)
                        * math.cos(((2 * y + 1) * v * math.pi) / 16)
                    )

            image[x][y] = 0.25 * total

    return image


# Level shift (-128)
def level_shift(block):
    return block - 128


# Reverse level shift (+128)
def reverse_shift(block):
    return block + 128
