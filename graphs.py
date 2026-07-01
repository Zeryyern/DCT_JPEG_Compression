"""
graphs.py
Visualization functions for JPEG DCT Compression
"""

import matplotlib.pyplot as plt
import numpy as np

# Histogram Comparison
def histogram(original, compressed):

    hist_original, _ = np.histogram(
        original,
        bins=256,
        range=(0,256)
    )

    hist_compressed, _ = np.histogram(
        compressed,
        bins=256,
        range=(0,256)
    )

    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    plt.plot(hist_original)
    plt.title("Original Histogram")
    plt.xlabel("Gray Level")
    plt.ylabel("Frequency")
    plt.xlim(0,255)

    plt.subplot(1,2,2)
    plt.plot(hist_compressed)
    plt.title("Compressed Histogram")
    plt.xlabel("Gray Level")
    plt.ylabel("Frequency")
    plt.xlim(0,255)

    plt.tight_layout()
    plt.show()


# Difference Image
def difference(original, compressed):

    diff = np.abs(original - compressed)

    plt.figure(figsize=(6,6))
    plt.imshow(diff, cmap="hot")
    plt.title("Difference Image")
    plt.colorbar()
    plt.axis("off")
    plt.show()


# PSNR Graph
def psnr_graph(qualities, psnr_values):

    plt.figure(figsize=(6,4))
    plt.plot(qualities, psnr_values, marker="o")
    plt.title("Quality vs PSNR")
    plt.xlabel("Quality Factor")
    plt.ylabel("PSNR (dB)")
    plt.grid(True)
    plt.show()


# MSE Graph
def mse_graph(qualities, mse_values):

    plt.figure(figsize=(6,4))
    plt.plot(qualities, mse_values, marker="o")
    plt.title("Quality vs MSE")
    plt.xlabel("Quality Factor")
    plt.ylabel("MSE")
    plt.grid(True)
    plt.show()