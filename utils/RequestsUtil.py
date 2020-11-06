# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/4 15:21
@Auth ： Yvon～₯㎕ζ๓
@File ：RequestsUtil.py
"""
import  requests
from utils.LogUtil import my_log

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

#创建封装post方法
def requests_post(url,json = None,headers = None):
    #1、发送get请求
    r = requests.post(url,headers = headers,json = json)
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

"""重构"""
#1、重建类
class Request:
#2、定义公共方法
    def __init__(self):
        self.log = my_log("Requests")
    #1、增加方法参数，根据参数来验证get/post,请求
    def requests_api(self,url,data = None,json = None,headers = None,cookies = None,method = 'get'):
        if method == "get":
            #get请求
            self.log.debug("发送get请求")
            r = requests.get(url, data = data,headers = headers,json = json,cookies = cookies)
        elif method == "post":
            #post请求
            self.log.debug("发送post请求")
            r = requests.post(url, data = data, headers=headers, json=json,cookies = cookies)
    #2、重复内容复制进来
        #获取结果相应内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        #内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        #4、字典返回
        return res
#3、重构get\post方法
    #1、get 定义方法
    def get(self,url,**kwargs):
    #2、定义参数
        #url,json,headers,cookies,method
    #3、调用公共方法
        return self.requests_api(url,method = 'get',**kwargs)
    #1、post 定义方法
    def post(self,url,**kwargs):
    #2、定义参数
        #url,json,headers,cookies,method
    #3、调用公共方法
        return self.requests_api(url,method = 'post',**kwargs)
