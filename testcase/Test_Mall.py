# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/3 20:06
@Auth ： Yvon～₯㎕ζ๓
@File ：Test_Mal.py
"""

"""
登录成功：http://211.103.136.242:8064/authorizations/
post请求2	
json {"username":"python","password":"12345678"}
"""
import pytest,json
from utils.RequestsUtil import requests_get,requests_post,Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from common.Base import init_db

'''初始化'''
request = Request()

#登录
# 1、导入包
import  requests,json
# 2、定义登录方法
def test_Login():
# 3、定义测试数据
     conf_y = ConfigYaml() #加载config.Conf文件中的ConfigYaml类
     url_path = conf_y.get_conf_url() # 读取配置文件中的url
     url = url_path + "/authorizations/" # 拼接url+登录参数
     # url = "http://211.103.136.242:8064/authorizations/"
     data = {"username":"python","password":"12345678"}
# 4、发送Post请求
#      r = requests_post(url,json = data)
     r = request.post(url,json = data)

# 5、输出结果
#      print(json.dumps(r,sort_keys=True,ensure_ascii = False,indent=4,separators=(', ', ': ')))  #Json格式打印

     #验证返回状态码
     code = r["code"]
     # assert code == 200
     #调用assert封装函数
     AssertUtil().assert_code(code,200)

     #验证返回结果内容
     # body = json.dumps(r["body"])
     # assert '"user_id": 1, "username": "python"' in body
     body = r["body"]
     # print(body)
     # AssertUtil().assert_in_body(body,'"user_id": 1')
     AssertUtil().assert_in_body(body,'"username": "python"')
     print("***************************************************************************************************")

#数据库断言
     #1、初始化数据库对象
     conn = init_db("db_1")
     #2、查询结果
     res_db = conn.fetchone("select id,username from tb_users where username = 'python'")
     print("数据库查询结果:",res_db)
     #3、数据库断言
     user_id = body["user_id"]
     assert user_id == res_db["id"]
# 6、返回token
     result_token = r['body']['token']
     # print(result_token)
     return result_token


"""
获取正确的个人信息：http://211.103.136.242:8064/user/	
前置条件：登录   get请求
 headers: { 'Authorization': 'JWT ' + this.token}
"""

# 定义个人信息方法
def test_info():
    #1、参数
    url = "http://211.103.136.242:8064/user/"
    token = test_Login()
    headers = {'Authorization': 'JWT ' + token}
    #2、get请求
    # r = requests_get(url,headers = headers)
    '''初始化'''
    request = Request()
    r = request.get(url,headers = headers)
    # result = r.json()
    #3、输出结果
    # print(r)
    print(json.dumps(r, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))


"""
商品信息："http://211.103.136.242:8064/categories/115/skus/"	
get 请求	
json   {"page":"1", "page_size": "10","ordering": "create_time"}       
"""

# 定义商品列表信息方法
def test_goodlist():
    #1、参数
    url = 'http://211.103.136.242:8064/categories/115/skus/'
    date = {"page":"1","page_size": "10","ordering": "create_time"}
    #2、get请求
    r = requests.get(url,json = date)

    #3、输出结果
    result = r.json()
    print(json.dumps(result,sort_keys=True,ensure_ascii = False,indent=4,separators=(', ', ': ')))


"""
购物车信息："http://211.103.136.242:8064/cart/"
前置条件：登录   post请求
json  {"sku_id": "3","count": "1", "selected": "true"}
headers: { 'Authorization': 'JWT ' + this.token} 	
"""
#定义添加购物车方法
def test_cart():
    #1、参数
    url = "http://211.103.136.242:8064/cart/"
    token = test_Login()
    headers = {'Authorization': 'JWT ' + token}
    date= {"sku_id": "3","count": "1", "selected": "true"}
    #2、Post请求
    r = requests.post(url, headers=headers,json = date)
    result = r.json()
    #3、输出结果
    print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))


"""
订单信息："http://211.103.136.242:8064/orders/"
前置条件：登录   post请求
json  {"address":"1","pay_method":"1"}
headers: { 'Authorization': 'JWT ' + this.token} 	
"""
#定义订单方法
def test_orders():
    #1、参数
    url = "http://211.103.136.242:8064/orders/"
    token = test_Login()
    headers = {'Authorization': 'JWT ' + token}
    date = {"address":"1","pay_method":"1"}
    #2、Post请求
    r = requests.post(url, headers=headers, json=date)
    result = r.json()
    #3、输出结果
    print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))


if __name__ == "__main__" :

    # test_Login()
    # test_goodlist()
    # test_cart()
    # test_orders()

    #1、根据默认运行原则、调整py文件命名，函数命名
    #2、pytest。main()运行
    pytest.main(['-s'])


