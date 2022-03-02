# @Time : 2020/3/8 10:29 
# @Author : FAN_Y
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from py2neo import Graph
import json
import sqlite3
from ICH_app import calculate_cosine
from ICH_app import cos_entity
from ICH_app import extract_from_graph
import time

graph=Graph("http://localhost:7474")

def readsqlite(sqlitepath, index,tag):
    mydb = sqlite3.connect(sqlitepath)
    cursor = mydb.cursor()  # 创建一个游标
    if tag=='QA':   #找QA库中的答案
        cursor.execute("SELECT 问题, 答案 FROM qa WHERE 序号=%d"%(index+1))
    elif tag=='search_detail':     #找项目的详细信息
        cursor.execute("SELECT project,info FROM detail WHERE project='{}'".format(index))
    elif tag=='search_path':
        cursor.execute("SELECT project,path FROM img WHERE project='{}'".format(index))
        print('okcursor1')
    #print(index)
    contents = cursor.fetchall()
    print('okcursor2')
    cursor.close()
    print(contents[0][1])
    return contents[0][1]

def extract_entity(mylist):
    entities = []
    words = []
    for id, item in enumerate(mylist):
        word = item.split('/')[0]
        words.append(word)
        tag = item.split('/')[1]
        if tag[0] == 'B':
            start = id
        if tag[0] == 'E':
            end = id
            entities.append([start, end, tag[2:]])
            #print(entities)
    entitydict = {}
    for e in entities:   #entities是[[0, 1, 'project'], [5, 6, 'feature_a']]这种list
        start = e[0]
        end = e[1]
        tag = e[2]
        #print(start, end, tag)
        #print(words[start], words[end])
        entitydict[''.join(words)[start:end+1]] = tag     #字典类型的
    #print(entitydict)
    return entitydict

def ReadFromJson(path):
    with open(path, 'r')as f:
        return json.load(f)

def info_search(yourquestion):
    # 如果图谱中找不到结果，使用sqlite中内容
    index, similarity = calculate_cosine.main(yourquestion)
    #print(index, similarity)
    if similarity > 0.4 :
        answer = readsqlite(r'ICH_app\ICH_data\ICH_QA.sqlite3', index,'QA')
    else:
        answer = '对不起，您的问题超出了我的知识范围，建议您移步至百度。'
    return answer

def qa(yourquestion):
    #形成实体和其标签的字典
    solved = NNmain.evaluate_line(yourquestion.replace(' ', ''))[0]   ## 使用神经网络来查找实体
    entitydict = extract_entity(solved)
    print(entitydict)
    try:
        print('in_search')
        object_label_set = set()
        subject_property_set = set()
        subject = ""
        object = ""
        subject_property = ""
        where_para = ""
        #下面根据实体和标签的字典，构造查询式中的每一部分
        for name, label in entitydict.items():
            if '_y' in label:   #客体实体
                object_label = label.split('_y')[0]   #比如：学派的label：school
                if object_label not in object_label_set:
                    object = '(object:%s)' % object_label
                    object_label_set.add(object)
            elif '_a' in label:  #对属性的查询
                subject_property = label.split('_a')[0]
                if subject_property not in subject_property_set:
                    subject_property = "subject.%s" % subject_property
                    subject_property_set.add(subject_property)
            else:    #主体实体
                subject = '(subject:%s)' % label    #主体实体的标签
                where_para = "subject.name=~'.*%s.*'" % name    #主体实体的名称
                #where_para = "subject.name='%s'" % name
                pbefore=name
                t=label

        #下面进行查询
        if subject_property:   #属性查询
            query = """
                MATCH %s
                where %s
                return %s,subject.name
            """ % (subject, where_para, subject_property)
            result= graph.run(query).data()
            print('这里是图谱返回的结果')
            #print(type(result))
            print(result)
            if result:
                print('121ok')
                answer = result[0][subject_property]
                p=result[0]['subject.name']
                #print(result[1][subject.name])
            else:
                answer = info_search(yourquestion)
                p=''
        elif object:            #实体间的查询
            query = """
                MATCH %s-[r]->%s
                where %s
                return subject, object,subject.name
            """ % (subject, object, where_para)
            result = graph.run(query).data()
            if result:
                print(result)
                answerlist = []
                for i in range(len(result)):  # 循环是因为一个项目会有多个所属省份、或者多个传承人
                    answerlist.append(result[i]['object']['name'])
                answer = " ".join(answerlist)
                p=result[len(result) - 1]['subject.name']
            else:
                answer = info_search(yourquestion)
                p=''
        else:
            answer = info_search(yourquestion)
            p=''
    except:
        answer = info_search(yourquestion)
        p=''
    print('ok150')
    print(answer)
    if p!='':    #有主要实体时，进行子图抽取
        entitydict[p]=entitydict.pop(pbefore)
        ret_graph=extract_from_graph.extract_graph(entitydict,graph) #在这里进行子图抽取
        print('here1')
        print(ret_graph)
        print('here2')
        detail=''
        path=''
        if t=='project':   #只有当查询主题是项目时，才会去查找相关信息和图片
            print('here3')
            detail=readsqlite(r'ICH_app\ICH_data\ICH_QA.sqlite3',p,'search_detail')
            print('这个项目的详细信息是：',detail)
            path=readsqlite(r'ICH_app\ICH_data\ICH_QA.sqlite3',p,'search_path')
            print('地址为：',path)
    else:    #普通问题，即关于非遗定义性问题，不去查找相关项目信息、图片地址、子图
        detail=''
        path=''
        ret_graph=[]
    return answer,detail,ret_graph,path


'''
def main():
    #start=time.time()
    qa('围棋的特点是什么')
    #end=time.time()
    #print('************程序执行用时：',end-start)
if __name__ == '__main__':
    main()
'''