# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/6 15:59
@Auth ： Yvon～₯㎕ζ๓
@File ：Conf.py
"""
import os
from utils.YamlUtil import YamlReader

#1、获取项目基本目录
#获取当前项目的绝对路径
current = os.path.abspath(__file__)
# print(current) # D:\InterAutoTest_W\config\Conf.py
# BASE_DIR = os.path.dirname(current) #D:\InterAutoTest_W\config
# print(BASE_DIR)
BASE_DIR = os.path.dirname(os.path.dirname(current)) #D:\InterAutoTest_W
# print(BASE_DIR)
#定义config目录路径
_config_path = BASE_DIR + os.sep + "config"
# print(_config_path)
#定义conf.yml文件路径
_config_file = _config_path + os.sep + "conf.yml"
# print(_config_file)


def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

#2、读取配置文件
#创建类
class ConfigYaml:
#初始化读取yaml配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
    #定义方法获取重要信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    print(conf_read.get_conf_url())

