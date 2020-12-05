# -*- coding: utf-8 -*-
# @Time : 2020/11/20 16:03
# @File : Base.py
# @Author : Yvon_Fajin

from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
import re,json

p_data = '\${(.*)}\$'

#1、定义init_db方法
def init_db(db_alias):
#2、初始化数据信息、通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])  # "7090"是一个字符串,故要转换int类型
    # port = db_info["db_port"]
#3、初始化mysql对象
    conn = Mysql(host,user,password,db_name,charset ,port )
    print(conn)
    return conn

def json_parse(data):
    """
    格式化字符,转换json
    :param data:
    :return:
    """
    # # 判断headers是否存在，json转义，无需
    # if headers:
    #     header = json.loads(headers)
    # else:
    #     header = headers
    return json.loads(data) if data else data


def res_find(data,pattern_data = p_data):
    """
    查询
    :param data:
    :param pattern_data:
    :return:
    """
    # pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res

def res_sub(data,replace,pattern_data = p_data):
    """
    替换
    :param data:
    :param replace:
    :param pattern_data:
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
       return re.sub(pattern_data,replace,data)
    return re_res

#验证请求中是否有依赖结果的
def params_find(headers,cookies):
    """
    验证请求中是否有${}$需要结果关联
    :param headers:
    :param cookies:
    :return:
    """
    if '${' in headers:
        headers = res_find(headers)
    if '${' in cookies:
        headers = res_find(cookies)

    return headers,cookies


if __name__ == "__main__":
    # init_db("db_1")
    print(res_find('{"Authorization": "JWT ${token}$"}'))
    print(res_sub('{"Authorization": "JWT ${token}$"},"123"'))


