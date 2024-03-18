
datapath = './corpus/raw/GossipCop.text.label.txt'

with open(datapath, 'r') as f:
    lines = f.readlines()
    labels = []
    texts = []
    for line in lines:
        List = line.split('\t')
        labels.append(List[2].strip())
        texts.append(List[3].strip())

    with open('./corpus/GossipCop.labels.txt', 'w') as f:
        f.write('\n'.join(labels))

    with open('./corpus/GossipCop.texts.txt', 'w') as f:
        f.write('\n'.join(texts))