"""
utils.py
Utility functions for JPEG DCT Compression
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# Load image and convert to grayscale
def load_image(path):
    img = Image.open(path).convert("L")
    return np.array(img, dtype=np.float64)


# Save reconstructed image
def save_image(image, path):
    image = np.clip(image, 0, 255).astype(np.uint8)
    Image.fromarray(image).save(path)


# Split image into 8x8 blocks
def split_blocks(image):

    h, w = image.shape
    blocks = []

    for i in range(0, h, 8):
        for j in range(0, w, 8):

            block = image[i:i+8, j:j+8]

            if block.shape == (8, 8):
                blocks.append(block)

    return blocks


# Merge blocks back into one image
def merge_blocks(blocks, shape):

    h, w = shape
    image = np.zeros(shape)

    index = 0

    for i in range(0, h, 8):
        for j in range(0, w, 8):

            image[i:i+8, j:j+8] = blocks[index]
            index += 1

    return image


# Show one image
def show_image(image, title="Image"):

    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.title(title)
    plt.axis("off")
    plt.show()


# Show original and compressed images
def compare_images(original, compressed):

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap="gray", vmin=0, vmax=255)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(compressed, cmap="gray", vmin=0, vmax=255)
    plt.title("Compressed")
    plt.axis("off")

    plt.tight_layout()
    plt.show()