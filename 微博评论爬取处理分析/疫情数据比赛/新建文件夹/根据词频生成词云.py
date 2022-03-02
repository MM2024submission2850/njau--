# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:59:51 2020

@author: 13284
"""
from os import path
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from PIL import Image

# 二值化处理
def cv():
    im = Image.open(r"C:\Users\13284\Desktop\1.png")
    Lim = im.convert('L')
    threshold = 185
    table=[]
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    bim = Lim.point(table, '1')
    bim.save('11.jpg')

# 生成词云
def create_word_cloud():
    frequencies = {}
    for line in open(r"C:\Users\13284\Desktop\4.txt",encoding='utf-8'):
        arr = line.split(" ")
        frequencies[arr[0]] = float(arr[1])
    # 支持中文, SimHei.ttf可从以下地址下载：https://github.com/cystanford/word_cloud
    d=path.dirname(__file__)
    img = np.array(Image.open(path.join(d, "11.jpg")))
    wc = WordCloud(
        font_path="C:/Windows/Fonts/simfang.ttf",
        max_words=100,
        width=2000,
        height=1200,
        background_color='white',
        mask=img,
    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file(r"C:\Users\13284\Desktop\4.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

# 根据词频生成词云
create_word_cloud()