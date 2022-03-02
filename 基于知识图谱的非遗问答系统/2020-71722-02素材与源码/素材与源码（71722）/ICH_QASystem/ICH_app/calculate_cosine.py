# @Time : 2020/3/7 10:58 
# @Author : FAN_Y
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from gensim import corpora,models,similarities
import sqlite3
import jieba
import json

path_dict1=r'ICH_app\ICH_data\userdict.txt'
path_stw = r'ICH_app\ICH_data\stopwords.txt'

def SaveToJson(path, content):
	with open(path, 'w')as f:
		json.dump(content, f)

def ReadFromJson(path):
	with open(path, 'r')as f:
		return json.load(f)

def read_txt(path):
    with open(path,'r', encoding='utf-8') as f:
        essay = f.readlines()
    stwords = []
    for e in essay:
    	if e.strip() != '':
    		stwords.append(e.strip())
    return stwords

def readsqlite(sqlitepath):
    mydb = sqlite3.connect(sqlitepath)
    cursor = mydb.cursor()  # 创建一个游标

    cursor.execute("SELECT 序号, 问题 FROM qa;")
    contents = cursor.fetchall()
    return contents

def cut_movestw(string):
	'该部分先分词，再去掉停用词，以列表的形式返回'
	jieba.load_userdict(path_dict1)
	stwords = read_txt(path_stw)
	seg_txt = jieba.cut(string)
	newstring_list = []
	for word in seg_txt:
		if word not in stwords:
			newstring_list.append(word)
	return newstring_list

def matchnewQ(question):
	'计算与该问题最最相似的问句'
	# 首先要加载这些保存的变量
	corpus = ReadFromJson(r'ICH_app\ICH_data\corpus.json')
	myword_dict = ReadFromJson(r'ICH_app\ICH_data\myword_dict.json')
    #计算语料库中每个文档向量的tfidf
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]
    #将用户输入的问题分词、向量化，转换成tf-idf向量
	string_list = cut_movestw(question)
	new_vec = [(myword_dict[word], string_list.count(word)) for word in string_list if word in myword_dict.keys()]
	new_vec_tfidf=tfidf[new_vec]
	#print(new_vec_tfidf)
    #为了准备相似度查询，我们需要输入所有我们我们需要比较的文档。
	index = similarities.MatrixSimilarity(corpus_tfidf)
    #实施查询
	sims = list(index[new_vec_tfidf])
	#print('索引是：', sims.index(max(sims)))
	print('相似度为（QA库）：', max(sims))
	return sims.index(max(sims)), max(sims)

def washdocuments(documents):
    '抽取出每一条文档，去掉停用词；创建字典并保存到json；向量化所有的问题并保存'
    dim2list = []
    for line in documents:   #line是tuple类型
        ID = line[0]
        document = line[1]
        newdoc_list = cut_movestw(document)
        dim2list.append(newdoc_list)
    dictionary = corpora.Dictionary(dim2list)
    #print(dictionary.token2id)
    SaveToJson('myword_dict.json', dictionary.token2id)  # 这个保存字典类型的变量

    # 将每一篇文档转换为向量
    corpus = [dictionary.doc2bow(text) for text in dim2list]   #词袋模型
    SaveToJson('corpus.json', corpus)
    # 初始化一个tfidf模型,可以用它来转换向量（词袋整数计数）表示方法为新的表示方法（Tfidf 实数权重）
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    # # 下面这两行的原因是没法直接保存gensim对象，所以转化成二维列表保存了。
    save_corpus_tfidf = [doc for doc in corpus_tfidf]
    SaveToJson("corpus_tfidf.json", save_corpus_tfidf)  # 保存每一个文档的表示方法，但是注意这个是一个二维列表；当进入一个新的句子时，要调用这个进行预测

def main(yourquestion):
	#content = readsqlite('ICH_QA.sqlite3')
	#pprint(content)
	# print('\n\n\n\n\n\n\n----------------------------------------------')
	#washdocuments(content)

	# yourquestion = '我们为什么要进行非物质文化遗产普查' # 32 相似度为： 0.706184
	# yourquestion = '文化遗产日是几月几号' # 8 相似度为： 0.83139515

	# yourquestion = '设立文化遗产日的倡议是谁提出的' # 49 相似度为： 0.8795184
	# yourquestion = '哪位专家提出了设立文化遗产日的建议' # 49 相似度为： 0.46190983

	#index,similarity = matchnewQ('我们为什么要进行非物质文化遗产普查')
	return matchnewQ(yourquestion)

if __name__ == '__main__':
	main(yourquestion)