import gzip
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn



def load_images(filename):
    with gzip.open(filename, 'rb') as f:

        # MNIST image file header
        magic, num_images, rows, cols = struct.unpack(
            ">IIII",
            f.read(16)
        )

        # Read all pixel data
        data = np.frombuffer(
            f.read(),
            dtype=np.uint8
        )

        # Convert to (number of images, 28, 28)
        images = data.reshape(
            num_images,
            rows,
            cols
        )
        return images



def load_labels(filename):
    with gzip.open(filename, 'rb') as f:

        # MNIST label file header
        magic, num_labels = struct.unpack(
            ">II",
            f.read(8)
        )

        print("Magic number:", magic)
        print("Number of labels:", num_labels)

        labels = np.frombuffer(
            f.read(),
            dtype=np.uint8
        )

        return labels



MNIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mnist")

train_images = load_images(
    os.path.join(MNIST_DIR, "train-images-idx3-ubyte.gz")
)

train_labels = load_labels(
    os.path.join(MNIST_DIR, "train-labels-idx1-ubyte.gz")
)

test_images = load_images(
    os.path.join(MNIST_DIR, "t10k-images-idx3-ubyte.gz")
)

test_labels = load_labels(
    os.path.join(MNIST_DIR, "t10k-labels-idx1-ubyte.gz")
)


print("\nTrain images:", train_images.shape)
print("Train labels:", train_labels.shape)

print("Test images:", test_images.shape)
print("Test labels:", test_labels.shape)

