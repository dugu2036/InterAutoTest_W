# -*- coding: utf-8 -*-
# @Time : 2020/11/6 19:45
# @File : pytest_demo.py
# @Author : Yvon_₯㎕ζ๓

import pytest

#1、创建简单测试方法
"""
1、创建普通方法
2、使用Pytest断言方法
"""
# 普通方法
def func(x):
    return x + 1

# 断言方法
def test_a():
    print("---test_a-----")
    assert  func(3) == 5 #断言失败

def test_b():
    print("---test_b-----")
    assert  1  #断言

#2、Pytest运行
"""
1、代码直接运行
2、命令行运行
"""
# 代码直接运行
if __name__ == "__main__":
    pytest.main(['-s',"pytest_demo.py"])