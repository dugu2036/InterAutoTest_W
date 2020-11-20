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

#定义db_conf.yml文件路径
_db_config_file = _config_path + os.sep + "db_conf.yml"
print(_db_config_file)

# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"
# print(_log_path)

#***************************************定义方法**************************************

def get_config_path():
    """
    获取config文件夹目录
    :return:
    """
    return _config_path

def get_log_path():
    """
    获取log文件路径
    :return:
    """
    return _log_path

def get_config_file():
    return _config_file

def get_db_config_file():
    """
    获取数据库配置文件
    :return:
    """
    return _db_config_file




#2、读取配置文件
#创建类
class ConfigYaml:

    def __init__(self):
        # 初始化读取yaml配置文件
        self.config = YamlReader(get_config_file()).data()
        # 初始化读取数据库yaml配置文件
        self.db_config = YamlReader(get_db_config_file()).data()
    #定义方法获取重要信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]

    def get_db_conf_info(self,db_alias):
        """
        根据db_alias获取该名称下的数据库信息
        :param db_alias:
        :return:
        """
        return self.db_config[db_alias]

if __name__ == "__main__":
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    print(conf_read.get_db_conf_info("db_1"))

