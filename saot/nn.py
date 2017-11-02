import torch
from torch.autograd import Variable


# A network with fully connected layers
class NeuralNetwork:
    def __init__(self, num_input, num_output, num_hidden = 100):
        self.num_hidden = num_hidden
        self.num_input = num_input
        self.num_output = num_output
        self.model = torch.nn.Sequential(
            torch.nn.Linear(num_input, self.num_hidden),
            torch.nn.ReLU(),
            torch.nn.Linear(self.num_hidden, num_output)
        )
        self.loss = torch.nn.MSELoss()
        self.trainer = torch.optim.Adam(self.model.parameters(), lr=1e-4)

    def train(self, input, groundtruth, num_steps = 10000):
        for i in range(num_steps):
            pred = self.model(Variable(input))
            loss = self.loss(pred, Variable(groundtruth))
            self.trainer.zero_grad()
            loss.backward()
            self.trainer.step()

    def eval(self, input):
        return self.model(Variable(input))
