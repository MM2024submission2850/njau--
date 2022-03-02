# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:55:52 2020

@author: 13284
"""
import re

import os
def fun(path):
    fileArray = []    
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'/'+fn)
            fileArray.append(eachpath)
    return fileArray 

def chuli(path):
    file =open(path,'r',encoding='utf-8')
    content = file.read()
    rawResults = re.findall(">.*?<",content,re.S)
    firstStepResults  = []
    for result in rawResults:
        #print(result)
        if ">\'][\'<"  in result:
            continue
        if ">:<"  in result:
            continue
        if ">回复<"  in result:
            continue
        if "><"  in result:
            continue
        if ">\', \'<"  in result:
            continue
        if "@"  in result:
            continue
        if "> <"  in result:
            continue
        else:
            firstStepResults.append(result)
    subTextHead = re.compile(">")
    subTextFoot = re.compile("<")
    i = 16
    for lastResult in firstStepResults:
        resultExcel1 = re.sub(subTextHead, '', lastResult)
        resultExcel = re.sub(subTextFoot, '', resultExcel1)
        print(i,resultExcel)
        i+=1
        with open(path,'w',encoding='utf-8') as fp:
            fp.write('\n')
            fp.write(resultExcel)
def main():
    path="测试"
    fileArray=fun(path)
    for raw_file_path in fileArray:
        chuli(raw_file_path)
        print(raw_file_path+"已经完成")
        
if __name__ == '__main__':
    main()