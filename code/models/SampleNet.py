from torch import nn


class SampleNet(nn.Module):
    def __init__(self):
        super(SampleNet, self).__init__()
        encoder = nn.Sequential(
            nn.Linear(5, 5),
            nn.Linear(5, 13)
        )
        classifier = nn.Softmax()

    def forward(self, x):
        return self.classifier(self.encoder(x))