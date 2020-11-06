# -*- coding: utf-8 -*-
# @Time : 2020/10/26 20:15
# @File : LogUtil.py
# @Author : Yvon_₯㎕ζ๓

import logging

#封装工具类
#定义日志级别的映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}
#1、创建类
class Logger:
#2、定义参数
    #输出文件名称,loggername,日志级别
    def __init__(self,log_file,log_name,log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level
#3、编写输出控制台或文件
        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 设置log级别
        self.logger.setLevel(log_l[self.log_level])
        # 判断handlers是否存在
        if not self.logger.handlers:
            # 输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level]) # logging.INFO
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
            fh_stream.setFormatter(formatter)
            # 写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            # 添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
