# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:11:47 2020

@author: 13284
"""
import codecs
import jieba
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import imageio

def get_words(txt):
    #进行分词
    list = jieba.cut(txt)
    c = Counter()

    #给分词定义条件进行筛选统计词频
    for x in list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1

    #打开一个文本将统计好的词频存放进去
    with open(r'C:\Users\13284\Desktop\新建文件夹\allcipin.txt', 'w', encoding='gbk') as fw:
        for (k, v) in c.most_common():
            fw.write(k + ' ' + str(v) + '\n')
        fw.close()

    #绘制词云图
 #   pac_mask = imageio.imread(r'e:\1000.png')
  #  wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=2000, mask=pac_mask).fit_words(c)
   # plt.imshow(wc)
    #plt.axis('off')
    #plt.show()
    #wc.to_file('e:\\26.png')

if __name__ == '__main__':
    #打开需要分词的文本
    with codecs.open(r'C:\Users\13284\Desktop\新建文件夹\all.txt', 'r', 'utf-8') as f:
        txt = f.read()
    get_words(txt)
