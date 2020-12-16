# -*- coding: utf-8 -*-
# @Time : 2020/12/7 17:09
# @File : allure_demo.py
# @Author : Yvon_Fajin

import pytest,allure

@allure.feature("公司在线接口测试系统,一级功能模块标签")
class TestCompany:
    @allure.title("测试用例标题1")
    @allure.description("执行登录试用例")
    @allure.story("子公司接口系统: 新电")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        print("新电")

    @allure.title("测试用例标题2")
    @allure.description("执行下单测试用例")
    @allure.story("子公司接口系统: 北极光")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("北极光")

    @allure.title("测试用例标题3")
    @allure.description("执行个人中心测试用例")
    @allure.story("子公司接口系统: 通付盾")
    def test_3(self):
        print("通付盾")

    @pytest.mark.parametrize("Company",["新电","北极光","通付盾"])
    def test_Company(self,Company):
        print(Company)
        allure.dynamic.title(Company)


if __name__ == '__main__':

    pytest.main(["-s","allure_demo2.py"])
