import jieba

s = input();
result_list = list(jieba.cut(s, cut_all=False))
print(result_list)

