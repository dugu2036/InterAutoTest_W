# -*- coding: utf-8 -*-
# @Time : 2020/11/6 20:37
# @File : pytest_class.py
# @Author : Yvon_₯㎕ζ๓

"""
1、定义类
2、创建测试方法test开头
3、创建setup_class，teardown_class
4、运行查看结果
"""
import  pytest

#1、定义类
class TestFunc:

    #3、创建setup，teardown
    def setup_class(self):
        print("---setup_class---")

    def teardown_class(self):
        print("---teardown_class---")

    #2、创建测试方法test开头
    def test_a(self):
        print("---新北通---")

    def test_b(self):
        print("---花道永徐龙莉张娟---")

#4、运行查看结果
if __name__ == "__main__":
    pytest.main(['-s','pytest_class.py'])