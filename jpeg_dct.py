"""
jpeg_dct.py
Implementation and Visualization of JPEG Compression
using Manual Discrete Cosine Transform (DCT)

Author: Zayyanu Awwal
"""

import numpy as np

from utils import *
from dct import *
from quantization import *
from metrics import *
from graphs import *


# JPEG Compression Function

def compress(image_path, quality):

    print("\nLoading image...")

    original = load_image(image_path)
    print("Shape:", original.shape)
    print("Data type:", original.dtype)
    unique = np.unique(original)
    print("Number of the unique gray level", len(unique))
    print("First 30 gray lvels:", unique[:30])
    blocks = split_blocks(original)

    reconstructed_blocks = []

    quantized_blocks = []

    first_block = None
    first_dct = None
    first_quantized = None
    first_reconstructed = None

    for index, block in enumerate(blocks):

        shifted = level_shift(block)

        dct_block = dct_2d(shifted)

        q_block = quantize(dct_block, quality)

        dequant = inverse_quantize(q_block, quality)

        recon = idct_2d(dequant)

        recon = reverse_shift(recon)

        reconstructed_blocks.append(recon)

        quantized_blocks.append(q_block)

        if index == 0:

            first_block = block

            first_dct = dct_block

            first_quantized = q_block

            first_reconstructed = recon

    reconstructed = merge_blocks(
        reconstructed_blocks,
        original.shape
    )

    output_path = "output/compressed_Q{}.png".format(quality)

    save_image(reconstructed, output_path)

    mse_value = mse(original, reconstructed)

    psnr_value = psnr(mse_value)

    original_coeff = len(quantized_blocks) * 64

    compressed_coeff = count_nonzero(quantized_blocks)

    ratio = compression_ratio(
        original_coeff,
        compressed_coeff
    )

    print("\nCompression Completed")

    print("---------------------------")

    print("Image Shape :", original.shape)

    print("Quality     :", quality)

    print("MSE         :", round(mse_value,4))

    print("PSNR        :", round(psnr_value,2), "dB")

    print("Compression :", round(ratio,2), ":1")

    print("Saved To    :", output_path)

    return (
        original,
        reconstructed,
        first_block,
        first_dct,
        first_quantized,
        first_reconstructed,
        mse_value,
        psnr_value
    )


# Main Program

qualities = []
mse_values = []
psnr_values = []

while True:

    print("\n======================================")
    print(" JPEG Compression using Manual DCT")
    print("======================================")

    image_path = input("\nEnter image path : ")

    quality = int(input("Enter Quality (1-100): "))

    (
        original,
        reconstructed,
        first_block,
        first_dct,
        first_quantized,
        first_reconstructed,
        mse_value,
        psnr_value

    ) = compress(image_path, quality)

    qualities.append(quality)
    mse_values.append(mse_value)
    psnr_values.append(psnr_value)

    while True:

        print("\n============== MENU ==============")

        print("1. Show Original Image")

        print("2. Show Compressed Image")

        print("3. Compare Images")

        print("4. Difference Image")

        print("5. Show First 8x8 Block")

        print("6. Show DCT Matrix")

        print("7. Show Quantized Matrix")

        print("8. Show Reconstructed Block")

        print("9. Histogram")

        print("10. PSNR Graph")

        print("11. MSE Graph")

        print("12. Compress Another Image")

        print("0. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            show_image(original, "Original")

        elif choice == "2":

            show_image(reconstructed, "Compressed")

        elif choice == "3":

            compare_images(
                original,
                reconstructed
            )

        elif choice == "4":

            difference(
                original,
                reconstructed
            )

        elif choice == "5":

            print("\nFirst 8x8 Block\n")

            print(first_block.astype(int))

        elif choice == "6":

            print("\nDCT Matrix\n")

            print(np.round(first_dct,2))

        elif choice == "7":

            print("\nQuantized Matrix\n")

            print(first_quantized.astype(int))

        elif choice == "8":

            print("\nReconstructed Block\n")

            print(first_reconstructed.astype(int))

        elif choice == "9":

            histogram(
                original,
                reconstructed
            )

        elif choice == "10":

            psnr_graph(
                qualities,
                psnr_values
            )

        elif choice == "11":

            mse_graph(
                qualities,
                mse_values
            )

        elif choice == "12":

            break

        elif choice == "0":

            print("\nThank you.")

            exit()

        else:

            print("Invalid choice.")