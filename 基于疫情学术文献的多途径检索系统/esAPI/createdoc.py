#encoding=utf-8

from esAPI.ESsetting import *
import requests
import json

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

