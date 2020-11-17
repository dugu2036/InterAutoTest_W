# -*- coding: utf-8 -*-
# @Time : 2020/11/6 20:13
# @File : pytest_func.py
# @Author : Yvon_₯㎕ζ๓

"""
1、定义类
2、创建测试方法test开头
3、创建setup，teardown
4、运行查看结果
"""
import  pytest

#1、定义类
class TestFunc:

    #3、创建setup，teardown
    def setup(self):
        print("---setup---")

    def teardown(self):
        print("---teardown---")

    #2、创建测试方法test开头
    def test_a(self):
        print("---新北通---")

    def test_b(self):
        print("---花道永徐龙莉张娟---")

#4、运行查看结果
if __name__ == "__main__":
    pytest.main(['-s','pytest_func.py'])