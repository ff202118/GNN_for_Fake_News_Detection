# GNN_for_Fake_News_Detection
### Introduction

​		将假新闻检测视为**图分类**和**节点分类**问题，比较这两种方法在性能和适用范围上的差异。其中图分类方法采用TextING，节点分类方法采用TextGCN。

​		在图分类问题中，构建每个新闻文档的独立图，借助门控图神经网络学习每个节点的细粒度表示，然后将所有节点信息聚合成文档级表示。

​		在节点分类问题中，构建基于整个语料库的异构图，并利用图注意力网络来捕捉全局共现信息，学习预测性的单词和文档嵌入，进而识别假新闻。  

####  Result and Analysis



|       Dataset       | 图分类 | 节点分类 |
| :-----------------: | :-----: | :-----: |
|      GossipCop      | 79.13%  | 79.25%  |
|  GossipCop(masked)  | 78.09%  | 77.23%  |
| GossipCop(replaced) | 76.65%  | 75.34%  |

​		通过表格，可以发现TextGCN在性能上略优于TextING。个人认为这种性能差距是因为TextGCN的全局共现特性更能学习到整个语料库的特征。TextGCN能够更好地捕捉文本数据中的全局关系和语境信息，从而对语料库的特征有更全面的理解。相比之下，TextING可能更注重局部特征的学习，对于整个语料库的特征表达可能略显不足，导致其在性能上稍逊于TextGCN。

​		尽管两者性能差距并不明显，但是基于图分类的方法有一个巨大优势——**归纳式学习**，即**从训练样本中学习的规则可以直接应用在测试样本中**。而基于节点分类的方法却是**直推式学习**，它需要**同时使用训练样本和测试样本来训练模型**，这就意味着当面临一个全新的数据时，需要重新训练模型。

​		在**模拟归纳**实验中，我们设计了两种归纳条件——**训练集掩码处理**和**测试集同义词替换**。通过实验结果，可以看到TextING在归纳条件下的表现是要优于TextGCN。可能的原因在于TextING对于单个文档构建文本图，能够捕捉到局部的细粒度表示，相较于TextGCN的全局感知，这种细粒度表示在遇到新单词时变现更佳。

​		综上所述，基于图分类的方法更适用于**及时、快速地对少量样本进行识别**。而基于节点分类的方法更适用于**对大量样本进行准确地识别**。

​		我的目的是开发一个假新闻检测系统，系统场景是用户可以自己输入新闻文本，模型对其进行自动识别。很明显，场景特点更符合图分类方法，所以后续系统开发会选择基于图分类的方法。

####  Reference

[1]	Zhang Y, Yu X, Cui Z, et al. Every document owns its structure: Inductive text classification via graph neural networks[J]. arXiv preprint arXiv:2004.13826, 2020.

[2]	Yao L, Mao C, Luo Y. Graph convolutional networks for text classification[C]//Proceedings of the AAAI conference on artificial intelligence. 2019, 33(01): 7370-7377.
