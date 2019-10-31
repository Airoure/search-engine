#  建索引
from doc import Doc

import jieba

import math

class Indexer:

    inverted = {}   # 记录词所在文档及词频

    idf = {}         # 词的逆文档频率

    id_doc = {}     # 文档与词的对应关系

 

    def __init__(self, file_path):

        self.doc_list = []

        self.index_writer(file_path)

 

    def index_writer(self, file_path):

        with open(file_path, 'r', encoding='utf-8') as f:

            for line in f.readlines():

                key, title, link = line.strip().split('\t\t')

                doc = Doc()

                doc.add('key', key)

                doc.add('title', title)

                doc.add('link', link)

                self.doc_list.append(doc)

        self.index()

 

    def index(self):

        doc_num = len(self.doc_list)     # 文档总数

        for doc in self.doc_list:

            key = doc.get('key')

            # 正排

            self.id_doc[key] = doc

 

            # 倒排

            term_list = list(jieba.cut_for_search(doc.get('title')))   # 分词

            for t in term_list:

                if t in self.inverted:

 

                    if key not in self.inverted[t]:

                        self.inverted[t][key] = 1

                    else:

                        self.inverted[t][key] += 1

                else:

                    self.inverted[t] = {key: 1}

 

        for t in self.inverted:

            self.idf[t] = math.log10(doc_num / len(self.inverted[t]))

 

        print("inverted terms:%d" % len(self.inverted))

        print("index done")

 

if __name__ == '__main__':

    print("index")

    Indexer("docs.txt")
