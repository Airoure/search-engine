import jieba

s = input();
result_list = list(jieba.cut(s, cut_all=False))  # 精确模式
result1_list = list(jieba.cut(s, cut_all=True))  # 全模式
result2_list = list(jieba.cut(s))  # 搜索引擎模式
print(result_list)
print(result1_list)
print(result2_list)
