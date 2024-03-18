import time
from sklearn import metrics
from torch import nn
import torch
from config import *
from dataset import get_data_loader
from model import Model
import warnings

# 忽略特定类型的警告
warnings.filterwarnings("ignore", category=UserWarning)

def train_eval(cate, loader, model, optimizer, loss_func, device):
    model.train() if cate == "train" else model.eval()
    preds, labels, loss_sum = [], [], 0.

    for i in range(len(loader)):
        loss = torch.tensor(0., requires_grad=True).float().to(device)

        for j, graph in enumerate(loader[i]):
            graph = graph.to(device)
            targets = graph.y
            y = model(graph)
            loss += loss_func(y, targets)
            preds.append(y.max(dim=1)[1].data)
            labels.append(targets.data)

        loss = loss / len(loader[i])

        if cate == "train":
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        loss_sum += loss.data
    preds = torch.cat(preds).tolist()
    labels = torch.cat(labels).tolist()
    loss = loss_sum / len(loader)
    acc = metrics.accuracy_score(labels, preds) * 100
    return loss, acc, preds, labels


if __name__ == '__main__':
    dataset = "GossipCop"

    print("load dataset")
    # params
    batch_size = 4096  # 反向传播时的batch
    mini_batch_size = 64  # 计算时的batch
    lr = 0.01
    dropout = 0.5
    weight_decay = 0.
    hid_dim = 96
    freeze = True
    start = 0

    num_classes = args[dataset]['num_classes']
    (train_loader, test_loader, valid_loader), word2vec = get_data_loader(dataset, batch_size, mini_batch_size)
    num_words = len(word2vec) - 1

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = Model(num_words, num_classes, word2vec=word2vec, hid_dim=hid_dim, freeze=freeze)
    loss_func = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)

    model = model.to(device)

    print("-" * 50)
    print(f"params: [start={start}, batch_size={batch_size}, lr={lr}, weight_decay={weight_decay}]")
    print("-" * 50)
    print(model)
    print("-" * 50)
    print(dataset)

    best_acc = 0.
    for epoch in range(start + 1, 300):
        t1 = time.time()
        train_loss, train_acc, _, _ = train_eval("train", train_loader, model, optimizer, loss_func, device)
        valid_loss, valid_acc, _, _ = train_eval("valid", valid_loader, model, optimizer, loss_func, device)
        test_loss, test_acc, preds, labels = train_eval("test", test_loader, model, optimizer, loss_func, device)

        if best_acc < test_acc:
            best_acc = test_acc

        cost = time.time() - t1
        print((f"epoch={epoch:03d}, cost={cost:.2f}, "
               f"train:[{train_loss:.4f}, {train_acc:.2f}%], "
               f"valid:[{valid_loss:.4f}, {valid_acc:.2f}%], "
               f"test:[{test_loss:.4f}, {test_acc:.2f}%], "
               f"best_acc={best_acc:.2f}%"))

    print("Test Precision, Recall and F1-Score...")
    print(metrics.classification_report(labels, preds, digits=4))
    print("Macro average Test Precision, Recall and F1-Score...")
    print(metrics.precision_recall_fscore_support(labels, preds, average='macro'))
    print("Micro average Test Precision, Recall and F1-Score...")
    print(metrics.precision_recall_fscore_support(labels, preds, average='micro'))