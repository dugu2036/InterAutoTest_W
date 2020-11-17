# -*- coding: utf-8 -*-
# @Time : 2020/11/17 16:39
# @File : pytest_two.py
# @Author : Yvon_₯㎕ζ๓

"""
1、创建类和测试方法
2、创建数据
3、创建参数化
4、运行
"""
import pytest

#1、创建类和测试方法
class TestDemo:

    #2、创建测试数据
    date_list = [("新电","花道永"),("北极光","徐龙莉"),("通付盾","张娟")]

    #3、参数化
    @pytest.mark.parametrize(('company',"manager"),date_list)

    def test_a(self,company,manager):
        print("test_a")
        print(company,manager)
        assert 1


if __name__ == "__main__":
    pytest.main(["pytest_two.py"])