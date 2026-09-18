from torch import nn


class NeuralNetwork(nn.Module):

    def __init__(self):
        super().__init__()


        self.network = nn.Sequential(
            nn.Linear(784,256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,10),
        )

    def forward(self, x):
        return self.network(x)