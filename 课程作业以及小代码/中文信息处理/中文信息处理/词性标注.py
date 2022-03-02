import random
import os

def fun(path):
	fileArray = []
	for root, dirs, files in os.walk(path):
		for fn in files:
			eachpath = str(root+'/'+fn)
			fileArray.append(eachpath)
	return fileArray

def read_and_divide(result,path):
	#result=list()
	f=open(path, 'r', encoding='utf-8', errors='ignore')
	lines = f.readlines()
	for line in lines:
		line=line.strip()
		if not len(line):
			continue
		sentence=""
		for word in line:
			word=word.strip()
			if word !="。":
				sentence=sentence+word
			else:
				text=sentence+"。"
				result.append(text)
				sentence=""

	f.close()
	return result
	#print(result)

def output(file,sentences):
	txt=open(file,"w",encoding="utf-8")
	for sentence in sentences:
		sentence=sentence.split("/")
		for word in sentence:
			word=word.strip()
			if len(word)==0:
				continue
			text=""
			if len(word)==1:
				text=word +"\t"+"S"
			else:
				if len(word)==2:
					text=word[0]+"\t"+"B"+"\n"+word[1]+"\t"+"E"
				else:
					if len(word)>2:
						for i in range (len(word)):
							if i ==0:
								text=word[0]+"\t"+"B"+"\n"
							else:
								if i==len(word)-1:
									text =text+word[i]+"\t"+"E"+"\n"
								else:
									text=text+word[i]+"\t"+"M"+"\n"
				txt.write(text)
				txt.write("\n")
			txt.write("\n")
	txt.close()


def main():
	path=r"分词结果"
	fileArray=fun(path)
	result=list()
	for i in fileArray:
		result=read_and_divide(result,i)
	random.shuffle(result)
	print(result)
	num=int(len(result)*0.1)
	text_txt=result[0:num]
	train_txt=result[num:]
	output("train.txt",train_txt)
	output("text.txt",text_txt)


if __name__ == '__main__':
	main()






