import random

import torch

from saot.nn import NeuralNetwork

# To learn f(a, b) = a + b
if __name__ == '__main__':
    # build
    net = NeuralNetwork(2, 1)
    # train
    input = [(random.randint(0, 100), random.randint(0, 100)) for i in range(1000)]
    truth = [a + b for (a, b) in input]
    net.train(torch.FloatTensor(input), torch.FloatTensor(truth))
    # validate
    more_input = [(random.randint(0, 100), random.randint(0, 100)) for i in range(20)]
    eval = net.eval(torch.FloatTensor(more_input))
    for i in range(len(more_input)): print more_input[i], eval[i].data[0]
