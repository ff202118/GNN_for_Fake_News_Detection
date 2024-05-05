import json
import random

with open('./data/raw/GossipCop.json', 'r') as f:
    data = json.load(f)

corpus = []

for index, item in enumerate(data):
    label = '0' if item['label'] == "fake" else '1'
    corpus.append(label + '\t' + item['text'])


train_size = int(0.8 * len(corpus))
test_size = len(corpus) - train_size

train = corpus[:train_size]
test = corpus[train_size:]

cnt = 0

for i, item in enumerate(train):
    train[i] = '\t' + 'train' + '\t' + train[i]

train = sorted(train, key=lambda x: x.split('\t')[2], reverse=True)

for i, item in enumerate(test):
    test[i] = '\t' + 'test' + '\t' + test[i]

test = sorted(test, key=lambda x: x.split('\t')[2], reverse=True)


all = train + test

for i, item in enumerate(all):
    all[i] = str(i) + all[i]

string = '\n'.join(all)
with open('./data/raw/GossipCop.text.label.txt', 'w') as f:
    f.write(string)


with open('./data/raw/GossipCop.text.label.txt', 'r') as f:
    lines = f.readlines()
    text = []
    ind = []
    for line in lines:
        text.append(line.split('\t')[3].strip())
        ind.append('\t'.join(line.split('\t')[:3]))

    with open('./data/text_dataset/corpus/GossipCop.txt', 'w') as f:
        f.write('\n'.join(text))

    with open('./data/text_dataset/GossipCop.txt', 'w') as f:
        f.write('\n'.join(ind))
