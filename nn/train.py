import random

import torch
from torch import nn
from matplotlib import pyplot as plt

from model import NeuralNetwork
from dataset import X_train, y_train, X_test, y_test



X_train = X_train.reshape(X_train.shape[0], 784)
X_test = X_test.reshape(X_test.shape[0], 784)

X_train = X_train / 255.
X_test = X_test / 255.

y_train = y_train.long()
y_test = y_test.long()

test_index = random.randint(0, y_test.shape[0] - 1)

model = NeuralNetwork()

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 20
losses = []

for _ in range(epochs):
    model.train()

    loss = 0

    predictions = model(X_train)

    loss = criterion(predictions, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    losses.append(loss.item())


with torch.no_grad():
    test_outputs = model(X_test)
    test_predictions = torch.argmax(test_outputs, dim=1)

    test_correct = (
        test_predictions == y_test
    ).sum().item()

    test_accuracy = (
        test_correct/ y_test.shape[0]
    )
    print(f"test_accuracy = {test_accuracy * 100}")




    img = X_test[test_index].reshape(28,28)
    plt.imshow(img, cmap="gray")
    plt.title(f"Actual value: {y_test[test_index]} Predicted Value: {test_predictions[test_index]}")
    plt.axis("off")
    plt.show()
    

