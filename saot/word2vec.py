import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Model(nn.Module):
    def __init__(self, ctx_size, emb_size, voca_size):
        super(Model, self).__init__()
        self.embeddings = nn.Embedding(voca_size, emb_size)
        self.linear = nn.Linear(emb_size, voca_size)

    def forward(self, inputs):
        pass

class Word2Vec:
    def train(self, tweet_set):
        vocabulary = set(w for tweet in tweet_set for w in tweet.split())
        voca_len = len(vocabulary)
        word_to_idx = {word: i for i, word in enumerate(vocabulary)}

    def eval(self, tweet):
        pass
