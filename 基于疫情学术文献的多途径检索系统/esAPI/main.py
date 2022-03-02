#encoding=utf-8
import re

import requests
import json
LOCALHOST="http://127.0.0.1:9200"
LOCALURL=LOCALHOST

header={'Content-Type':'application/json'}

def createDOC(index_type,index_name,data_json,unique_id="-1"):
    tmp_url=LOCALURL+"/"+index_type+"/"+index_name
    if(unique_id!="-1"):
        tmp_url=tmp_url+"/"+str(unique_id)
    response=requests.post(tmp_url,data=json.dumps(data_json),headers=header)
    return response.status_code

def createIndex(index_type,data_json,number_of_shards=3,number_of_replicas=1):
    tmp_url=LOCALURL+"/"+index_type+"/"
    data={
        "settings": {
            "index": {
                "number_of_shards": number_of_shards,
                "number_of_replicas": number_of_replicas
            }
        },
        "mappings": {
            "properties":data_json
        }
    }
    response=requests.put(tmp_url,data=json.dumps(data),headers=header)
    return response.status_code

def insertDoc(index_type,index_name,data_json):
    tmp_url = LOCALURL + "/" + index_type + "/"+ index_name
    response = requests.post(tmp_url,data=json.dumps(data_json),headers=header)
    return response





o_re=re.compile(r"<organism>(.*?)</organism>")
b_re=re.compile(r"<body>(.*?)</body>")
d_re=re.compile(r"<disease>(.*?)</disease>")
rug_re=re.compile(r"<drug>(.*?)</drug>")
t_re=re.compile(r"<therapeutic>(.*?)</therapeutic>")
s_re=re.compile(r"<sign>(.*?)</sign>")
c_re=re.compile(r"<check>(.*?)</check>")

class_re=re.compile(r"[abcdefop]")

re_dict={
    "organism":o_re,
    "body":b_re,
    "disease":d_re,
    "drug":rug_re,
    "therapeutic":t_re,
    "sign":s_re,
    "check":c_re
}

def Toclass(s):
    if(s=="p" or s=="n"):
        return "o"
    else:
        return s

def eval_null(data):
    try:
        tmp=eval(data)
        if(tmp):
            return tmp[0]
        else:
            return ""
    except:
        return ""

if __name__=="__main__":
    index_type="covid_doc"
    index_name="_doc"

    f=open(r"C:\Users\13284\Desktop\桌面4.1整理\file\1.txt","rt",encoding="utf-8")
    print("数据开始插入")
    for line in f.readlines():
        datas=line.replace("\r","").replace("\n","").split("\t")
        if(len(datas)<11):
            continue
        doc_class=[Toclass(_) for _ in class_re.findall(datas[0].lower())]
        entity=list(set([_.strip() for key in re_dict.keys() for _ in re_dict[key].findall(datas[1].lower())]))
        entity_ab=eval_null(datas[1])
        publisher=eval_null(datas[2])
        publisher_num=eval_null(datas[3])
        doi=eval_null(datas[4])
        date=eval_null(datas[5])
        title = eval_null(datas[6])
        if(eval_null(datas[7])):
            author = ";".join(eval_null(datas[7]))
        else:
            author = ""
        if (eval_null(datas[8])):
            institution = ";".join(eval_null(datas[8]))
        else:
            institution = ""
        abstract = eval_null(datas[9])
        keyword = eval_null(datas[10]).replace("  ","")
        data={
            "doc_class" : doc_class,
            "entity" : entity,
            "abstract_entity":entity_ab,
            "publisher" : publisher,
            "publisher_num" : publisher_num,
            "doi" : doi,
            "date" : date,
            "title" : title,
            "author" : author,
            "institution" : institution,
            "abstract" : abstract,
            "keyword" : keyword
        }
        print(data)

        statue=insertDoc(index_type,index_name,data)
        #statue=insertDoc(index_type,data)
        print(statue.text)
        print("数据已经插入")

    f.close()
    print("ok")