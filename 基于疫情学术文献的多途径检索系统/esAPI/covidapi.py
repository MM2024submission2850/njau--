#encoding=utf-8

from esAPI.ESsearch import *
import json

def read_relation():
    '''
    读取关键词图谱，并进行展示。返回的结构为字典，包括每个关键词，以及该关键词连接的目标对象

    :return:
    '''
    f = open("esAPI/relation.txt", "rt", encoding="utf-8")
    tmp_dict={}
    for line in f.readlines():
        datas=line.replace("\r","").replace("\n","").split("\t")
        if(len(datas)<4):
            continue
        tmp_dict[datas[0]]=tmp_dict.get(datas[0],[])
        tmp_dict[datas[0]].append(
            {
                "sourceNode": datas[0],
                "sourceType":datas[1],
                "targetNode": datas[2],
                "targetType":datas[3],
                "relationName": datas[4],
                "value":int(datas[5])
            }
        )
    f.close()
    return tmp_dict

relation_dict = read_relation()

def searchword_engine(word,term_list=["abstract","entity"],from_page=0,size=10):
    '''
    根据关键字查询相关文献信息，

    :param word:所查询的关键词
    :param term_list:实体序列
    :param from_page:从那个位置开始照
    :param size:分为多少页
    :return:反回关键词图谱类，{数据量，查询结果}
    '''
    tmp_dict=json.loads(search_word("covid_doc","_doc",word,term_list,from_page=from_page,size=size))
    result=tmp_dict.get("hits",{})
    total_num=result.get("total",{}).get("value",0)
    serp_result=[data.get("_source",{}) for data in result.get("hits",[])]
    return {"total_num":total_num,"result":serp_result}


def searchfilter_engine(booldata,booletype="should",from_page=0,size=10):
    '''
    根据booldata组合查询论文实体
    example：booldata
    {
        "doc_class":"a",
        "entity":"mpro"
    }

    :param booldata:过滤条件
    :param booletype:
    :param from_page:
    :param size:查询量
    :return:
    '''
    tmp_dict = json.loads(search_filter("covid_doc", "_doc", booldata,booletype=booletype, from_page=from_page, size=size))
    result = tmp_dict.get("hits", {})
    total_num = result.get("total", {}).get("value", 0)
    serp_result = [data.get("_source", {}) for data in result.get("hits", [])]
    return {"total_num": total_num, "result": serp_result}

def get_graph(word="Corona Virus Disease 2019",max_node=10):
    '''
    获取关系图信息，其中关键字放在'relation.txt'文件中，已经有函数read_relation()完成了关系的读取。
    这里我们调用即可

    :param word:查询的源节点数据，获取的目标节点数据
    :param max_node:
    :return:
    '''
    tmp_list=relation_dict.get(word,[])
    sorted_list=sorted(tmp_list,key=lambda x:x["value"],reverse=True)
    filter_list=[sorted_list[i] for i in range(min(max_node,len(sorted_list)))]
    sum_value=sum([_["value"] for _ in filter_list])
    r_list=[]
    for tmp in filter_list:
        t_dict=tmp.copy()
        t_dict["value"]=float(t_dict["value"])/sum_value
        r_list.append(t_dict)
    return {"r":r_list}

if __name__=="__main__":
    relation_dict = read_relation()

    res1=searchword_engine(word="covid-2019")
    print(res1)
    booldata={
        "doc_class": "a",
        "entity": "mpro"
    }
    res2=searchfilter_engine(booldata)
    print(res2)
    res3=get_graph(word="Analytical:Diagnostic and Therapeutic Techniques: and Equipment")
    print(res3)