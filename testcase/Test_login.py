# -*- coding: utf-8 -*-
# @Time : 2020/11/23 20:22
# @File : Test_login.py
# @Author : Yvon_Fajin

from config.Conf import ConfigYaml
import pytest
from utils.RequestsUtil import Request

#1、获取测试用例内容list
#获取testlogin.yml文件路径
data_list = ConfigYaml().get_testlogin_conf_info()
# print(data_list)

@pytest.mark.parametrize("login",data_list)  # login 是定义的变量
#2、参数化执行测试用例

def test_yaml(login):
    #初始化url,data
    url = ConfigYaml().get_conf_url() + login["url"]
    # print("url %s"%url)
    data = login["data"]
    # print("data %s"%data)

    #post请求
    request = Request()
    res = request.post(url,json = data)
    print(res)

if __name__ == "__main__":
    pytest.main(["-s","Test_login.py"])