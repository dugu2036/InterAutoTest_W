# -*- coding: utf-8 -*-
# @Time : 2020/11/17 20:38
# @File : pytest_assert.py
# @Author : Yvon_₯㎕ζ๓

import pytest

#判断XX为真
#1、定义方法进行assert
def test_company():
    company = True
    assert company


#判断XX不为真
def test_manager():
    manager = True
    assert not manager


#判断b包含a
def test_managers():
     manager = "花道永"
     managers = ["花道永","徐龙莉","张娟"]
     assert manager in managers


#判断a==b
def test_time():
     time = times = "180211"
     assert time == times


#判断a!=b
def test_times():
     time = "180211"
     times = "170926"
     assert time != times

if __name__ == "__main__":
    pytest.main(["pytest_assert.py"])