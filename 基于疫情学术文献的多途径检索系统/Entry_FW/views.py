# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .apps import Entry_FWConfig
from urllib import request as rq
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt

# 加载esAPI模块
from esAPI.covidapi import *

app_name = Entry_FWConfig.name

# 一些获取信息的链接
# json格式的实时状况数据，包括国内和国外情况，国外部分位于 'thertotal'
rtjson = 'https://news.sina.com.cn/project/fymap/ncp2020_full_data.json?_=1591602512921&callback=jsoncallback'
# 实时新闻信息
rtnews = 'https://interface.sina.cn/news/country_epidemic_lists.d.json?page=1&pagesize=3&callback=country_epidemic&_=1591602512910'
# 湖北省历史数据
his_province = 'https://gwpre.sina.cn/interface/news/ncp/data.d.json?mod=china_hubei_history&callback=hbApi_data&_=1591602512906'


relation_dict = read_relation()

def test(request):
    '''
    用于前端调试Debug页面
    :param request:
    :return:
    '''
    if (not settings.DEBUG):
        return Http404()
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


def default_mainpage_data():
    '''
    抛弃使用

    :return:
    '''
    # (菜单名,图标), {菜单项:urls,...}
    mproject1 = (('统计区', 'fa-cog'),
                 {'关键词图谱': 'keywordmap','统计图表(实体)': 'sta', })
    mproject2 = (('检索区', 'fa-wrench'),
                 {'关键词、实体检索': 'search', '类别检索': 'search_class','图谱检索': 'tupujiansuo', })
    # [(文字，图，url),...]
    # rt_info = [('疫情趋势', 'fa-chart-area', 'rtinfo'), ('各国数据', 'fa-table', 'url2')]

    context = {
        'title': 'COVID-19知识图谱',
        'projects': [
            mproject1,
            mproject2,
        ],
        # 'rt_info': rt_info,
        'container': abstractpage(None)
        # 'container': researcher(None)
    }

    return context


def template_index(request, container=None):
    '''
    模块化的index
    :param request:
    :return:
    '''
    t_index = loader.get_template(app_name + '/FW_index_template.html')
    t_slider = loader.get_template(app_name + '/FW_silder_template.html')

    # 切换通用生成页面和 特定生成页面
    if (container == None):
        t_container = abstractpage(None)
    else:
        t_container = container

    # (菜单名,图标), {菜单项:urls,...}
    prepdata = default_mainpage_data()

    context = {
        "silder_template": t_slider.render(prepdata),
        "container_template": t_container
    }

    return HttpResponse(t_index.render(context, request))


def abstractpage(request):
    '''
    摘要页面，提供摘要信息的提取
    注意，其中的color项，包括有 color=(primary,success,info,warning,danger,secondary)
    :param request:
    :return:
    '''
    r = rq.urlopen(rtjson)
    rec = r.read()
    json_str = json.loads(rec[13:-2])  # 由于包含一些不合适的字符，在这里需要去掉
    othertotal = json_str['data']['othertotal']

    container = loader.get_template(app_name + '/cont_abstract.html')
    dataset = [('累积确诊', othertotal['certain'], 'primary'),
               ('现有确诊', int(othertotal['certain']) - int(othertotal['die']) - int(othertotal['recure']), 'info'),
               ('死亡', othertotal['die'], 'warning'),
               ('累积治愈', othertotal['recure'], 'success')]

    projects = [('疫苗研发', 20, 'primary'),
                ('病理研究', 50, 'success'),
                ('临床救治', 70, 'info'),
                ('医用物资生产', 30, 'warning'), ]
    context = {
        "dataset": dataset,
        # "project": projects,
    }
    if request == None:
        return container.render(context)
    else:
        return HttpResponse(container.render(context, request))


def rtinfo(request):
    '''
    实时信息显示，从api接口获取实时疫情信息，并显示在此。这里使用了其他网站的数据，直接渲染至此
    :param request:
    :return:
    '''
    r = rq.urlopen(rtjson)
    rec = r.read()
    json_str = json.loads(rec[13:-2])  # 由于包含一些不合适的字符，在这里需要去掉

    othertotal = json_str['data']['othertotal']
    container = loader.get_template(app_name + '/cont_rtinfo.html')
    dataset = [('累积确诊', othertotal['certain'], 'primary'),
               ('现有确诊', int(othertotal['certain']) - int(othertotal['die']) - int(othertotal['recure']), 'info'),
               ('死亡', othertotal['die'], 'warning'),
               ('累积治愈', othertotal['recure'], 'success')]

    context = {
        'dataset': dataset,

    }
    return HttpResponse(container.render(context, request))


def researcher(request):
    '''
    研究成果信息整理
    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/cont_researcher.html')
    return HttpResponse(container.render())


def template_search(request):
    '''
    对researcher模块化的实现

    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/FW_search_template.html').render()

    return HttpResponse(template_index(request, container=container))



def template_search_class(request):
    '''
    通过类别进行检索的页面。在主体部分，增加了类别按钮，每个按钮对应一个类别， 通过事件相应获取对应的类别，更新页面
    :param request:
    :return:
    '''

    # 分类名称，代号，色系 (primary,success,info,warning,danger,secondary)
    class_list = [
        ('有机体', 'A', 'danger'),
        ('解剖学', 'B', 'primary'),
        ('疾病', 'C', 'success'),
        ('化学药物', 'D', 'info'),
        ('分析诊断，治疗技术', 'E', 'warning'),
        ('现象与过程', 'F', 'secondary'),
    ]

    context={
        'classlist':class_list,
    }

    container = loader.get_template(app_name + '/FW_search_class_template.html').render(context)

    return HttpResponse(template_index(request, container=container))


def template_research_deatil(request):
    '''
    响应/search页面的请求，显示文献的详细信息
    :param request:
    :return:
    '''

    if (request.method == "GET"):
        doi = request.GET['doi']
        print('input doi:[{}]'.format(doi))

    # 在此处查找论文，同时渲染前端
    res = searchword_engine(word='COVID-19')

    article = res['result'][0]

    # 对数据的一些小修改
    ## 需要对检索结果的entity 进行去重
    entity = article['entity']
    entity_brief = []
    for x in entity:
        if (x not in entity_brief):
            entity_brief.append(x)
    article['entity'] = entity_brief

    ## doi信息修复
    doi = article['doi']
    doi = doi[5:-1]
    article['doi'] = doi

    # 构建内容，渲染网页
    context = {
        'data': article,
    }
    container = loader.get_template(app_name + '/FW_search_detail_template.html').render(context)

    return HttpResponse(template_index(request, container=container))


def keywordmappage(request):
    '''
    关键词图谱页面，与主界面内容一致
    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/cont_keywordmap.html')
    return HttpResponse(container.render(default_mainpage_data(), request))


def template_keywordmappage(request):
    container = loader.get_template(app_name + '/cont_keywordmap.html').render()
    gen_page = template_index(request, container=container)
    return HttpResponse(gen_page)


def keywordmapdata(request):
    '''
    用于生成关系图绘图所需的数据
    :param request:
    :return:
    '''
    data_dict = {}
    if (request.method == "GET"):
        data_dict = request.GET
    if (data_dict.get("word", "")):
        relation = get_graph(word=data_dict.get("word", ""))
    else:
        relation = get_graph()
    return JsonResponse(relation, safe=False)


@csrf_exempt
def request_doclist(request):
    '''
    用于响应用户的POST请求，同时根据用户的参数，返回所需的json信息

    :param request:
    :return: 返回数据项的关键词包括[total_num, result]，其中result是一个列表，记录了搜索结果，每一项包括12个成员
    这里的total_num是不准确的，需谨记
    搜索实例的成员:
    doc_class, entity, abstract_entity, publisher, publisher_num, doi, date, title, auther, institution, abstract, keyword

    '''
    if (request.method == "POST"):
        print(request.POST)
        mode = request.POST['mode']
        info = request.POST['info']

        if ("check_query" == mode):
            # 常规检索，这个是匹配摘要部分
            json_str = searchword_engine(word=info)
            return JsonResponse(json_str['result'], safe=False)

        if ("check_entry" == mode):
            # 根据实体进行检索，在标注的实体词中进行检索
            json_str=searchfilter_engine({"entity": info})
            return JsonResponse(json_str['result'], safe=False)

        if("check_class"==mode):
            # 根据类别进行检索，这个是按照已经整理的文献类别
            json_str = searchfilter_engine({"doc_class": info})
            return JsonResponse(json_str['result'], safe=False)

        return JsonResponse("error", safe=False)


@csrf_exempt
def request_graph(request):
    '''
    返回对图的查询信息
    :param request:
    :return:
    '''
    if (request.method == "POST"):
        info = request.POST['info']
        res = get_graph(info)
        return JsonResponse(res, safe=False)





def sta(request):
    '''
    对researcher模块化的实现

    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/blank.html').render()

    return HttpResponse(template_index(request, container=container))
def tupujiansuo(request):
    '''
    对researcher模块化的实现

    :param request:
    :return:
    '''
    container = loader.get_template(app_name + '/知识图谱.html').render()

    return HttpResponse(template_index(request, container=container))

