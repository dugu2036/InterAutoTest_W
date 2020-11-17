# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/5 19:24
@Auth ： Yvon～₯㎕ζ๓
@File ：yaml_demo.py
"""
"""
#1、创建yaml格式文件
#2、读取这个文件
#3、输出
"""
import yaml

# 读取单个文件
#1、导入yaml包

# #2、打开文件
# with open("./data.yml","r",encoding = 'utf-8') as f:
# #3、使用yaml读取文件
#     r = yaml.safe_load(f)
# #4、输出文件内容
#     print(r)

# 读取多个文件
#1、yaml多个文件读取方法，all
with open("./data.yml","r",encoding = 'utf-8') as f:
    r = yaml.safe_load_all(f)
#2、循环打印
    for i in r:
        print(i)

