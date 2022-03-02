#encoding=utf-8

from esAPI.ESsetting import *
import requests
import json

LOCALURL=LOCALHOST

header={'Content-Type':'application/json'}

def search_word(index_type,index_name,word,term_list=["abstract","entity"],from_page=0,size=10):
    tmp_url=LOCALURL+"/"+index_type+"/"+index_name+"/"+"_search"
    query_data={
        "from": from_page, "size": 500,
        "query": {
            "multi_match":{
                "query": word,
                "fields": term_list
            }
        },
        "sort":{
            "_score": {
            "order": "desc"
            }
        }
    }
    response=requests.post(tmp_url,data=json.dumps(query_data),headers=header)
    return response.text


def search_filter(index_type,index_name,booldata,booletype="should",from_page=0,size=10):
    tmp_url = LOCALURL + "/" + index_type + "/" + index_name+"/"+"_search"
    word_data=[]
    for key in booldata.keys():
        word_data.append( {"term" : { key : booldata[key] } })
    query_data = {
        "from": from_page, "size": 2000,
        "query": {
            "bool" : {
                 booletype : word_data,
                 "minimum_should_match" : len(word_data),
                 "boost" : 1.0
            }
        },
        "sort": {
            "_score": {
                "order": "desc"
            }
        }
    }
    response = requests.post(tmp_url, data=json.dumps(query_data), headers=header)
    return response.text