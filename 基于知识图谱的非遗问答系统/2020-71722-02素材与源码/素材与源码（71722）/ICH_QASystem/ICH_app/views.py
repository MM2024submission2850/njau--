from django.shortcuts import render,HttpResponse
from ICH_app.qa_entrance import qa
import json
# Create your views here.

def query(request):
    #return  HttpResponse("HELLO")
    if request.method=="POST":
        question=request.POST.get('Question')
        print('问题是：',question)
        answer,detail,ret_graph,path=qa(question)
        data,links=create_graph(ret_graph)
        result={
            'answer':answer,
            'detail':detail,
            'path':path,
            'nodes':data,
            'links':links,
        }
        return HttpResponse(json.dumps(result), content_type="application/json")
    else:
        return HttpResponse("请求错误")

def create_graph(k_graph):
    data = []
    links = []
    r_set = set()
    if k_graph!=[]:    #这里有待修改
        for n in k_graph.nodes:
            node_label = list(n.labels)[0]
            data.append({
                # "id": remote(n)._id,
                "name": n['name'],
                "category": node_label,    #数据项所在类目的index
                "symbolSize": 25,      #该类目节点标记的大小
                "draggable": "true",
                # "value": 27,
            })
        for r in k_graph.relationships:
            subject_node, object_node = r.nodes
            r_type = list(r.types())[0]
            if r_type not in r_set:
                r_set.add(r_type)
                data.append({
                    # 'id': remote(r)._id,
                    "name": r_type,
                    "category": '关系',
                    "symbolSize": 10,
                    "draggable": "true",
                    # "value": 27,
                })
            links.append({
                "source": subject_node['name'],
                "target": r_type,
            })
            links.append({
                "source": r_type,
                "target": object_node['name'],
            })
    print(data,links)
    return data, links

