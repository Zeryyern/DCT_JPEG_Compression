"""
metrics.py
Image Quality Metrics
"""

import numpy as np
import math


# Mean Squared Error (MSE)
def mse(original, reconstructed):

    return np.mean(
        (original.astype(np.float64) -
         reconstructed.astype(np.float64)) ** 2
    )


# Peak Signal-to-Noise Ratio (PSNR)
def psnr(mse_value):

    if mse_value == 0:
        return float("inf")

    return 10 * math.log10((255 ** 2) / mse_value)


# Estimate Compression Ratio
def compression_ratio(original_coefficients,
                      compressed_coefficients):

    if compressed_coefficients == 0:
        return float("inf")

    return original_coefficients / compressed_coefficients


# Count non-zero coefficients
def count_nonzero(blocks):

    total = 0

    for block in blocks:
        total += np.count_nonzero(block)

    return total