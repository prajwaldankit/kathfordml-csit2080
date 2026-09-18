import torch
from torch import nn
from matplotlib import pyplot as plt

from model import NeuralNetwork
from dataset import X_train, y_train, X_test, y_test

test_index = 42

plt.imshow(X_test[test_index])
plt.title(f"{y_test[test_index]}")
plt.show()

X_train = X_train.reshape(X_train.shape[0], 784)
X_test = X_train.reshape(X_train.shape[0], 784)

X_train = X_train / 255.
X_test = X_train / 255.

y_train = y_train.long()
y_test = y_test.long()

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
    output = model(X_test[test_index])
    prediction_new = torch.argmax(output)
    img = X_test[test_index].reshape(28,28)
    plt.imshow(img, cmap="gray")
    plt.title(f"Actual value: {y_test[test_index]} Predicted Value: {prediction_new}")
    plt.show()
    

