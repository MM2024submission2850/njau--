# @Time : 2020/2/29 11:11 
# @Author : FAN_Y
# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import  csv

def sort_person():
    df=pd.read_csv(r'C:\Users\axer\Desktop\person.csv',encoding='utf-8')
    col1 = list(df['人名'].values)
    col2 = list(df['项目编号'].values)
    dic={}
    for i in range(len(col1)):
        name=col1[i].split('，')
        for j in range(len(name)):
            dic.update({name[j]: col2[i]})
    df_new = pd.DataFrame.from_dict(dic,orient='index',columns=['person_num'])
    df_new = df_new.reset_index().rename(columns={'index':'id'})
    df_new.to_csv('person_sorted.csv')
    print('ok1')

def sort_area():
    df = pd.read_csv(r'C:\Users\axer\Desktop\belong_to.csv', encoding='utf-8')
    col1 = list(df['所属地区'].values)
    col2 = list(df['项目编号'].values)
    listall = []    #对于belong_to这种关系，一个地区会对应多个项目，方便起见不采用多值字典，改用列表
    for i in range(len(col1)):
        name = col1[i].split('，')
        for j in range(len(name)):
            listall.append([name[j],col2[i]])
    with open('belong_to.csv', 'a',newline='') as csv_file:   #如果不加newline=''会出现写一行空一行的情况
        writer = csv.writer(csv_file)
        for k in range(len(listall)):
            writer.writerow([listall[k][0],listall[k][1]])
    print('ok2')

def main():
    sort_person()
    sort_area()

if __name__ == '__main__':
    main()
