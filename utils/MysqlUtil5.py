# -*- coding: utf-8 -*-
# @Time : 2020/11/19 17:03
# @File : MysqlUtil.py
# @Author : Yvon_₯㎕ζ๓

#1、导入pymysql包
import pymysql
#2、连接database
conn = pymysql.connect(
    host = '211.103.136.242',
    user = 'test',
    password = 'test123456',
    database = "meiduo",
    charset = "utf8",
    port = 7090

)
#3、获取执行sql的光标对象
cursor = conn.cursor()
#4、执行sql
sql = "select username,password from tb_users"
cursor.execute(sql)
cursor.fetchone() #查询单条数据
res = cursor.fetchall()  #查询多条数据
print(res)
#5、关闭对象
cursor.close() #关闭光标
conn.close() # 关闭数据库