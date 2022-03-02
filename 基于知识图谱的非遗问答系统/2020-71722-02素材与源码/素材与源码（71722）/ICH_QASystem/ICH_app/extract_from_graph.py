# @Time : 2020/3/12 10:02 
# @Author : FAN_Y
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import json
from py2neo import Graph
#from py2neo import remote

graph=Graph("http://localhost:7474")

def extract_graph(entitydict,graph):
    #entitydict = find_entity(yourquestion)
    #entitydict={'苗族古歌':'project','特点':'feature_a'}
    entityshow = ['project', 'person', 'area', 'type']
    ret_graph = None
    for name, label in entitydict.items():
        if label in entityshow:    #如果是实体，而非属性
            inquirement1 = 'MATCH (n {name: "%s"})-[r]-(m) RETURN n, r, m' % name
            ret_data = graph.run(inquirement1).data()
            #print(type(ret_data))
            if ret_data:
                ret_graph = ret_data[0]['r']
                #print(ret_graph)
                for index in range(1, len(ret_data)):
                    #print(ret_data[index]['r'])
                    ret_graph = ret_graph | ret_data[index]['r']  #这里的 | 表示子图的并
    return ret_graph    #这里的ret_hraph就是符合查询条件的一个大的子图


#if __name__ == '__main__':
   #yourquestion='苗族古歌的特点是什么？'
#   extract_graph(graph)




