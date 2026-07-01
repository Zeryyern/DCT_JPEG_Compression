"""
quantization.py
JPEG Quantization Functions
"""

import numpy as np


# Standard JPEG Quantization Matrix
Q = np.array([
    [16,11,10,16,24,40,51,61],
    [12,12,14,19,26,58,60,55],
    [14,13,16,24,40,57,69,56],
    [14,17,22,29,51,87,80,62],
    [18,22,37,56,68,109,103,77],
    [24,35,55,64,81,104,113,92],
    [49,64,78,87,103,121,120,101],
    [72,92,95,98,112,100,103,99]
], dtype=np.float64)


# Generate Quantization Matrix based on Quality Factor
def get_quantization_matrix(quality):

    quality = max(1, min(quality, 100))
    if quality < 50:
        scale = 5000 / quality
    else:
        scale = 200 - 2 * quality

    q = np.floor((Q * scale + 50) / 100)

    q[q < 1] = 1

    return q


# Quantization
def quantize(dct_block, quality):

    q = get_quantization_matrix(quality)

    return np.round(dct_block / q)


# Inverse Quantization
def inverse_quantize(q_block, quality):

    q = get_quantization_matrix(quality)

    return q_block * q