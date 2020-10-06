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
from utils.YamlUtil import YamlReader

# res = YamlReader("./data.yml").data()
res = YamlReader("./data.yml").data_all()
print(res)




