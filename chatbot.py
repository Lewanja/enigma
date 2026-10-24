import math
import random


class Vocab:
    def __init__(self, text):
        words = sorted(set(text.split()))
        self.itos = ["<unk>","<bos>"] + words
        self.stoi = {w: i for i, w in enumerate(self.itos)}

    def encode():
        pass
    def decode():
        pass
    def __len__(self):
        pass