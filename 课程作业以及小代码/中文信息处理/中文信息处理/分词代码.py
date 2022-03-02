import xlrd
import codecs
import os

#批量读取文件夹里的路径
def fun(path):
    fileArray = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray
#读取要分词的文本，返回变成列表
def readfile(raw_file_path):
	with codecs.open(raw_file_path,"r",encoding="utf-8") as f:
		raw_file=f.readlines()
		return raw_file
#读取分词表
def readxls(path):
	xl=xlrd.open_workbook(path)
	sheet=xl.sheets()[0]
	data_list=list(sheet.col_values(1))[1:]
	return data_list

#逆向最大匹配法分词
def cut_words(raw_sentences,word_dic,stopwords_list):
	word_cut=[]
	max_length=max(len(word) for word in word_dic)      #最大的词长是分词词典中的最大词长，是出示分词的最大词长
	for sentence in raw_sentences:
		sentence=sentence.strip()							#strip函数返回一个没有首尾空白字符的（eg：‘\n ’'\t'''）的sentence，用来避免分词错误
		words_length=len(sentence)							#单个句子中的字数
		cut_word_list=[]									#储存切分出来的语句
		#判断句子是否切分完毕
		while words_length > 0:
			max_cut_length=min(words_length,max_length)
			for i in range (max_cut_length,0,-1):			#根据切片的性质，截取words_length中的词（从-i到-1）
				new_word=sentence[words_length-i:words_length]

				if new_word in word_dic:
					cut_word_list.append(new_word)
					words_length=words_length -i
					break
				if new_word in stopwords_list:
					words_length=words_length-i
					break
				elif i==1:
					cut_word_list.append(new_word)
					words_length=words_length-1
		cut_word_list.reverse()								#要把结果逆向输出
		words="/".join(cut_word_list)
		word_cut.append(words.lstrip("/"))					#最后要把句子首段的符号删掉，避免以后将分词结果转化成list的时候出现空的字符串元素
	return word_cut

#词频的统计
def count_cipin(content_cut):
	str="".join(content_cut)
	keywordnum={}
	for i in str.split("/"):
		if keywordnum.get(i) is None:						#是零的时候就建立一个否则加一
			keywordnum[i]=1
		else:keywordnum[i]=keywordnum[i]+1
	output=open ("词频统计.txt",'w')
	for i in keywordnum:
		output.write("%s-->%d\n"%(i,keywordnum[i]))
	#输出分词文本
def writetxt(output_path,sentences):
	with codecs.open(output_path,"a","utf-8") as f:  #在原来的基础上加
		for sentence in sentences:
			f.write(sentence)
	print ("ok txt")

def main():
	path="分词文本"
	fileArray=fun(path)
	for raw_file_path in fileArray:
		raw_file=readfile(raw_file_path)
		words_path=r"C:\Users\13284\Desktop\中文信息处理\词表\words.xlsx"
		stopwords_path=r"C:\Users\13284\Desktop\中文信息处理\词表\stopwords.xlsx"
		words_data=readxls(words_path)
		stopwords_data=readxls(stopwords_path)
		content_cut=cut_words(raw_file,words_data,stopwords_data)
		count_cipin(content_cut)
		outfile_path=raw_file_path[5:-4]+"分词结果.txt"
		writetxt(outfile_path,content_cut)
if __name__=='__main__':
	main()
	print("over")

