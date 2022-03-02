# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:05:42 2020

@author: 13284
"""


import jieba
 
txt = open(r"C:\Users\13284\Desktop\第一阶段1.23-2.17.txt", encoding="utf-8").read() #'wuxi.txt' 更换你的文件（txt格式）
def jiebafenci(txt,wordslist):
    jieba.load_userdict(r"C:\Users\13284\Desktop\1.txt")
    words  = jieba.lcut(txt) 
    counts = {}  
    for word in words:  
        counts[word] = counts.get(word,0) + 1  
    lst=[]
    for i in range(len(wordslist)):
        try :
            print(wordslist[i],counts[wordslist[i]])
        except:
            lst.append(wordslist[i])
    print('不存在的词:',lst)
if __name__=='__main__':
    txt = open(r"C:\Users\13284\Desktop\第一阶段1.23-2.17.txt", encoding="utf-8").read() #'wuxi.txt' 更换你的文件（txt格式）
    need_words = open(r"C:\Users\13284\Desktop\1.txt", encoding="utf-8").read() #这个是要查找的词的txt文件 每个词一行
    find=need_words.split()
    jiebafenci(txt,find)
