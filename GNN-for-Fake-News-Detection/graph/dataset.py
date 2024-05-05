from config import args
import joblib
import numpy as np
from torch_geometric.data import Data, DataLoader
import torch
import random
from tqdm import tqdm


class MyDataLoader(object):

    def __init__(self, dataset, batch_size, mini_batch_size=0):
        self.total = len(dataset)
        self.dataset = dataset
        self.batch_size = batch_size
        self.mini_batch_size = mini_batch_size
        if mini_batch_size == 0:
            self.mini_batch_size = self.batch_size

    def __getitem__(self, item):
        ceil = (item + 1) * self.batch_size
        sub_dataset = self.dataset[ceil - self.batch_size:ceil]
        if ceil >= self.total:
            random.shuffle(self.dataset)
        return DataLoader(sub_dataset, batch_size=self.mini_batch_size)

    def __len__(self):
        if self.total == 0: return 0
        return (self.total - 1) // self.batch_size + 1


def split_train_valid_test(data, train_size, valid_part=0.1):
    train_data = data[:train_size]
    test_data = data[train_size:]
    random.shuffle(train_data)
    valid_size = round(valid_part * train_size)
    valid_data = train_data[:valid_size]
    train_data = train_data[valid_size:]
    return train_data, valid_data, test_data


def get_data_loader(dataset, batch_size, mini_batch_size):
    # param
    train_size = args[dataset]["train_size"]

    # load data
    inputs = np.load(f"temp/{dataset}.inputs.npy")
    graphs = np.load(f"temp/{dataset}.graphs.npy")
    weights = np.load(f"temp/{dataset}.weights.npy")
    targets = np.load(f"temp/{dataset}.targets.npy")
    len_inputs = joblib.load(f"temp/{dataset}.len.inputs.pkl")
    len_graphs = joblib.load(f"temp/{dataset}.len.graphs.pkl")
    word2vec = np.load(f"temp/{dataset}.word2vec.npy")

    # py graph dtype
    data = []
    for x, edge_index, edge_attr, y, lx, le in tqdm(list(zip(
            inputs, graphs, weights, targets, len_inputs, len_graphs))):
        x = torch.tensor(x[:lx], dtype=torch.long)
        y = torch.tensor(y, dtype=torch.long)
        edge_index = torch.tensor([e[:le] for e in edge_index], dtype=torch.long)
        edge_attr = torch.tensor(edge_attr[:le], dtype=torch.float)
        lens = torch.tensor(lx, dtype=torch.long)
        data.append(Data(x=x, y=y, edge_attr=edge_attr, edge_index=edge_index, length=lens))

    # split
    train_data, test_data, valid_data = split_train_valid_test(data, train_size, valid_part=0.1)

    # return loader & word2vec
    return [MyDataLoader(data, batch_size=batch_size, mini_batch_size=mini_batch_size)
            for data in [train_data, test_data, valid_data]], word2vec