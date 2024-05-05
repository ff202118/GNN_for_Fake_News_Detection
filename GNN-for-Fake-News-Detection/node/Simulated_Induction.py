from utils import MaskWord, Count_word, syn


path = './data/text_dataset/corpus/'
p = 0.4

def Count():
    doc_list = []
    word_set = set()
    with open(f'{path}GossipCop.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            doc_list.append(line.strip())

    for doc in doc_list:
        test_word_list = doc.split(' ')
        for word in test_word_list:
            word_set.add(word)

    print(len(word_set))


if __name__ == '__main__':
    MaskWord(path, p)
    # syn(path, p)
