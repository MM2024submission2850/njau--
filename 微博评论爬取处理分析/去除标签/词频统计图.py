# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:18:47 2020

@author: 13284
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fig, ax = plt.subplots()
myfont = FontProperties(fname=r'C:\Windows.old\Windows\Fonts\simhei.ttf',size=12)
N = 10
words = []
counts = []
for line in open(r'C:\Users\13284\Desktop\去除标签\1.23zlcipin.txt'):
    line.strip('\n')
    words.append(line.split(' ')[0])
    counts.append(int(line.split(' ')[1].strip('\n')))
colors = ['#FA8072']

#绘制前十条数据（N=10）
rects = ax.barh(words[:N], counts[:N], align='center', color=colors)
ax.set_yticklabels(words[:N],fontproperties=myfont)
ax.invert_yaxis()
ax.set_title('高频词汇',fontproperties=myfont, fontsize=17)
ax.set_xlabel(u"出现次数",fontproperties=myfont)
plt.show()
