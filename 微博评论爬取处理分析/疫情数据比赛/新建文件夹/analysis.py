import xlrd
import jieba
import math
import os


def fun(path):
    file_array = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root + '/' + fn)
            file_array.append(eachpath)
    return file_array


def read_txt(path):
    f = open(path, 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()
    print("文本文件已完成读取 path:" + path)
    return lines


def read_excel(path):
    book = xlrd.open_workbook(path)
    sheet = book.sheets()[0]
    word_dic = {}
    word_dic["出行"] = sheet.col_values(0)
    word_dic["经济"] = sheet.col_values(1)
    word_dic["防护"] = sheet.col_values(2)
    word_dic["政治"] = sheet.col_values(3)
    word_dic["宣传"] = sheet.col_values(4)
    return word_dic


def count(data, word_dic):
    score = {"出行": 0, "经济": 0, "防护": 0, "政治": 0, "宣传": 0}
    for sen in data:
        seg_list = jieba.cut(sen)
        for word in seg_list:
            for key in word_dic.keys():
                if word in word_dic[key]:
                    score[key] += 1
    return score


def normalization(score):
    sum_of_squares = 0
    new_score = {}
    for key in score.keys():
        sum_of_squares += score[key] * score[key]
    square_root = math.sqrt(sum_of_squares)
    for key in score.keys():
        new_score[key] = score[key] / square_root
    return new_score


def main():
    word_dic = read_excel("程序用词典.xlsx")
    print(word_dic)
    txt_list = fun("./第四阶段")
    f = open("第阶段统计.txt", 'w+', encoding='utf-8')
    f.write("文档名\t出行\t经济\t防护\t政治\t宣传\n")
    for txt in txt_list:
        data = read_txt(txt)
        score = count(data, word_dic)
        # score = normalization(score)
        print(score)
        f.write(txt + "\t")
        f.write(str(score["出行"]) + "\t" + str(score["经济"]) + "\t" + str(score["防护"]))
        f.write("\t" + str(score["政治"]) + "\t" + str(score["宣传"]) + "\n")
    f.close()


if __name__ == '__main__':
    main()
