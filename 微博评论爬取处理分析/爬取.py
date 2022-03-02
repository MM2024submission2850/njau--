# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 07:36:47 2020

@author: 13284
"""

import requests
import re
import time
def get_one_page(url):#请求函数：获取某一网页上的所有内容
    headers = {
    'User-agent' : 'your User-agent',
    'Host' : 'weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie' : 'ALF=1595115608; _T_WM=63421932029; SCF=Ali5pQpakdAmQH9wQdxmFw5hgbS9yDB0oRo7SjIL6p2eqE6pHLtCd2FGWHibfGcK9GoF9m26zpBVr6aEjIy0Iu8.; MLOGIN=1; SUB=_2A25z74wrDeRhGeNN61YS8S_FzjWIHXVRExRjrDV6PUJbkdAKLRHukW1NSfW-b2_mupLWzJ9kaCJFBQkx-InvYh9a; SUHB=0N21siU9F3omJ3; SSOLoginState=1592523899; M_WEIBOCN_PARAMS=oid%3D4517418729340066%26luicode%3D10000011%26lfid%3D2304132803301701_-_WEIBO_SECOND_PROFILE_WEIBO; WEIBOCN_FROM=1110106030',
    'DNT' : '1',
    'Connection' : 'keep-alive'
     }#请求头的书写，包括User-agent,Cookie等
    response = requests.get(url,headers = headers,verify=False)#利用requests.get命令获取网页html
    if response.status_code == 200:#状态为200即为爬取成功
        return response.text#返回值为html文档，传入到解析函数当中
    return None
def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    with open('6.13#北京新发地市场45人咽拭子阳性#.txt','a',encoding='utf-8') as fp:
        fp.write(result)

for i in range(30):
    url = "https://weibo.cn/comment/J6qtQFsSR?uid=2803301701&rl=0&page="+str(i)
    html = get_one_page(url)
    print(html)
    print('正在爬取第 %d 页评论' % (i+1))
    parse_one_page(html)
    time.sleep(3)
