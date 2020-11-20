# -*- coding: utf-8 -*-
# @Time : 2020/11/19 17:03
# @File : MysqlUtil.py
# @Author : Yvon_₯㎕ζ๓

from utils.LogUtil import my_log
import pymysql

#1、创建封装类
class Mysql:
#2、初始化数据、连接数据库、光标对象
    def __init__(self,host,user,password,database,charset = "utf8",port = 3306):
        self.log = my_log()
        self.conn = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            charset = charset,
            port = port
           )
        # 获取执行sql的光标对象
        # self.cursor = self.conn.cursor()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor) #光标字典方式查询
#3、创建查询、执行方法

    def fetchone(self,sql):
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self,sql):
        """
        执行
        :param sql:
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()  # 提交
        except Exception as ex:
            self.conn.rollback() #数据库回滚
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

#4、关闭对象
    def __del__(self):

        #关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        #关闭连接对象
        if self.conn is not None:
            self.conn.close()



if __name__ == "__main__":
    mysql = Mysql('211.103.136.242','test','test123456',"meiduo",charset = "utf8",port = 7090)
    #res = mysql.fetchall("select username,password from tb_users") # 查询所有
    #print(res)
    Res = mysql.fetchone("select username,password from tb_users") # 查询1条
    print(Res)
    res = mysql.exec("update tb_users set first_name='张娟' where username ='18866666666'")
    print(res)

    # 数据放入配置文件
    #1、创建db_conf.yml,db1,db2
    #2、编写数据库相关信息
    #3、重构Conf.py文件
























"""
#1、导入pymysql包

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
"""


