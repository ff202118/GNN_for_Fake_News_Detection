import json
from utils import clean_str
from nltk.corpus import stopwords
import numpy as np

datapath = './GossipCop/'
dataset = 'GossipCop'

def clean():
    # 把原本的数据集合并
    with open(datapath + 'before/train.json', 'r') as f:
        train_data = json.load(f)
    with open(datapath + 'before/test.json', 'r') as f:
        test_data = json.load(f)
    with open(datapath + 'before/val.json', 'r') as f:
        val_data = json.load(f)

    with open(datapath + 'GossipCop.json', 'w') as f:
        json.dump(train_data + test_data + val_data, f)


    with open(datapath + dataset + '.json') as f:
        data = json.load(f)

    print(len(data))

    # 统计词频
    word_freq = {}
    for news in data:
        words = news['text'].split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    print(f"num of word: {len(word_freq)}, "
          f"max freq word: {max(word_freq, key=word_freq.get)}, "
          f"min freq word: {min(word_freq, key=word_freq.get)}")

    # 去除低频词和停用词
    stop_words = set(stopwords.words('english'))

    for news in data:
        words = news['text'].split()
        doc_words = []
        for word in words:
            if word_freq.get(word) >= 5 and word not in stop_words:
                doc_words.append(word)
        doc_str = ' '.join(doc_words).strip()
        doc_str = clean_str(doc_str)
        news['text'] = doc_str

    print(len(data))
    with open(datapath + dataset + '.json', 'w') as f:
        json.dump(data, f)

def statistics():
    with open(datapath + dataset + '.json', 'r') as f:
        data = json.load(f)

    lens = []
    for news in data:
        Set = set(news['text'].split())
        List = list(Set)
        doc_len = len(List)
        lens.append(doc_len)

    print(f"avg len: {sum(lens)/len(lens)} , max len: {max(lens)} , min len: {min(lens)}")


def data_split():
    with open(datapath + dataset + '.json', 'r') as f:
        data = json.load(f)

    print(len(data))

    cnt = 0
    for news in data:
        cnt += 1
        news['id'] = cnt

    data = np.array(data)
    np.random.shuffle(data)

    train_size = int(0.8 * len(data))
    test_size = len(data)-train_size

    train_data = data[:train_size].tolist()
    test_data = data[train_size:train_size+test_size].tolist()

    print(train_size, test_size, len(data))

    for news in train_data:
        news['cate'] = 'train'
    for news in test_data:
        news['cate'] = 'test'

    with open(datapath + dataset + '.json', 'w') as f:
        json.dump(train_data+test_data, f)


def map2index():
    with open(datapath + dataset + '.json', 'r') as f:
        data = json.load(f)

    labels = set()
    docs = []
    map_index = []

    for news in data:
        labels.add(news['label'])
        docs.append(news['text'])

    cnt = 0
    labels_map = {}
    for label in labels:
        labels_map[label] = cnt
        cnt += 1

    for news in data:
        map_index.append(f"{news['id']}\t{news['cate']}\t{labels_map[news['label']]}")

    with open(datapath + dataset + '.txt', 'w') as f:
        f.write('\n'.join(docs))
    with open(datapath + dataset + '.idx', 'w') as f:
        f.write('\n'.join(map_index))

if __name__=='__main__':
    # clean()
    # statistics()
    data_split()
    # map2index()
