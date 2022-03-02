# @Time : 2020/3/7 16:37 
# @Author : FAN_Y
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import jieba
import pandas as pd

path1=r'C:\Users\axer\Desktop\word2.txt'
path2=r'C:\Users\axer\Desktop\word.txt'
path3=r'D:\2020计设\问答题库\ICH_QA.csv'
path4='stopwords.txt'
path5='userdict.txt'

def read_txt(path):
    with open(path,'r', encoding='utf-8') as f:
        essay = f.readlines()
    stwords = []
    for e in essay:
    	if e.strip() != '':
    		stwords.append(e.strip())
    return stwords

def write_txt(path,wordlist):
    with open(path,'w',encoding='utf-8') as f:
        for i in wordlist:
            f.write(i+'\n')
    print('write_done')
    f.close()

def sort():
    stwords = read_txt(path4)
    df=pd.read_csv(path3,encoding='utf-8')
    col1 = list(df['问题'].values)
    jiebadict=[]
    listuser1=[]
    for i in range(len(col1)):
        text=jieba.cut(col1[i])
        for word in text:
            if word not in stwords:
                jiebadict.append(word)
    Jiebadict=list(set(jiebadict))   #jieba分词后的词典
    user1=read_txt(path1)
    for word in user1:   #对于杨挑出来的专有名词，如果这个词不在jieba的分词表中，说明jieba不能识别这个词，故添加进User1
        if word not in Jiebadict:
            listuser1.append(word)
    User1=list(set(listuser1))   #杨帆挑出的专有名词 终
    with open(path2,encoding='utf-8') as f:
        user2=f.readline()
    User2=user2.split('/')   #郭祥月挑出的专有名词
    for word in User2:
        if word not in Jiebadict and word not in User1:   #对于郭挑出的专有名词，如果不在这其余的两个列表中，则附加至User1
            User1.append(word)
    userdict=list(set(User1))
    write_txt(path5,userdict)
    print('ok')

def main():
    sort()

if __name__ == '__main__':
    main()