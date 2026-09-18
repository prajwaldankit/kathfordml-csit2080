import gzip
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import torch


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

X_train = torch.tensor(train_images, dtype=torch.float32)
y_train = torch.tensor(train_labels, dtype=torch.float32)

X_test = torch.tensor(test_images, dtype=torch.float32)
y_test = torch.tensor(test_labels, dtype=torch.float32)


# plt.imshow(train_images[34], cmap="gray")
# plt.title(f"{train_labels[34]}")
# plt.axis(False)
# plt.show()
