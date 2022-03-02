import codecs
import re
import jieba
import os
import xlrd


# 读取已分词的疫情病毒语料
def read_txt(txt_path):
    with open(txt_path, "r", encoding="UTF-8") as f:
        data = f.read()
        with open("1.23-2.17.txt", 'a', encoding='utf-8') as f2:
            f2.write(data)
        f.close()
        f2.close()
    return data


def read_word(path):
    with open(path, "r", encoding="UTF-8") as f:
        data = f.read()
        f.close()
    return data

# 获取停用词表
def getstopword(path):
    swlist = []
    excel = xlrd.open_workbook(path)
    sheet = excel.sheets()[0]
    swlist = list(sheet.col_values(1))[1:]  # 读取第二列的停用词
    print(swlist)
    print('Get stopwords!')
    return swlist

# 统计词性频次情况
def count_word(data, txt_path, swlist):
    words = jieba.lcut(data)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            if word in swlist:
                continue
            else:
                counts[word] = counts.get(word, 0)+1
        items = list(counts.items())
        items.sort(key=lambda x:x[1], reverse=True)

   # if len(items) <= 100:
    for i in range(len(items)):
        word, count = items[i]
        with open(txt_path, 'a', encoding='utf-8') as f:
            f.write("{0:<1}{1:>5}".format(word, count) + '\n')
            f.close()
  #  else:
   #     for i in range(100):
    #        word, count = items[i]
     #       with open(txt_path, 'a', encoding='utf-8') as f:
      #          f.write("{0:<1}{1:>5}".format(word, count) + '\n')
       #         f.close()


def main():
    filenames = os.listdir(r'./data')
    for file in filenames:
        read_txt(file)

    data = read_word('1.23-2.17.txt')
    swlist = getstopword('stopwords.xlsx')  # 获取停用词表
    count_word(data, '第一阶段1.23-2.17.txt', swlist)


    print('ok!')


if __name__ == '__main__':
    main()
