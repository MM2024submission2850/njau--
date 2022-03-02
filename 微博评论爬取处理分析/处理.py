# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 07:52:14 2020

@author: 13284
"""

# -*- coding: utf-8 -*
import re
file =open('6.13#北京新发地市场45人咽拭子阳性#.txt','r',encoding='utf-8')

content = file.read()
#content=''' '''

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
    with open(r'O:\wb\去除标签\6.13zl2.txt','a',encoding='utf-8') as fp:
        fp.write('\n')
        fp.write(resultExcel)
