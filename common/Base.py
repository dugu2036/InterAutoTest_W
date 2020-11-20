# -*- coding: utf-8 -*-
# @Time : 2020/11/20 16:03
# @File : Base.py
# @Author : Yvon_Fajin

from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql

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

if __name__ == "__main__":
    init_db("db_1")



