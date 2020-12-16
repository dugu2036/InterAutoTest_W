# -*- coding: utf-8 -*-
# @Time : 2020/12/7 17:09
# @File : allure_demo.py
# @Author : Yvon_Fajin

import pytest
import allure

@allure.feature("接口测试，这是一个一级标签")
class TestAllure:

    @allure.title("测试用例标题1")
    @allure.description("执行测试用例1的结果是test1")
    @allure.story("这是一个二级标签：test1")

    def test_1(self):
        print("test_1")

    @allure.title("测试用例标题2")
    @allure.description("执行测试用例2的结果是test2")
    @allure.story("这是一个二级标签：test2")

    def test_2(self):
        print("test_2")

    @allure.title("测试用例标题3")
    @allure.description("执行测试用例3的结果是test3")
    @allure.story("这是一个二级标签：test3")
    def test_3(self):
        print("test_3")




if __name__ == '__main__':

    pytest.main(["-s","allure_demo.py"])
