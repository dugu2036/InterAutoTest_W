# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/4 14:40
@Auth ： Yvon～₯㎕ζ๓
@File ：T_requests.py
"""
import  requests

#创建封装get方法
def requests_get(url,headers):
    #1、发送get请求
    r = requests.get(url,headers = headers)
    #2、获取结果相应内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    #3、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
    #4、字典返回
    return res

