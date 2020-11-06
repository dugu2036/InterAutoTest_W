# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/6 19:26
@Auth ： Yvon～₯㎕ζ๓
@File ：log_demo
"""
#1、导入logging包
import logging
#2、设置配置信息
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
#3、定义日志名称
logger = logging.getLogger("log_demo")
#4、info,debug
logger.info("info")
logger.debug("debug")
logger.warning("warning")