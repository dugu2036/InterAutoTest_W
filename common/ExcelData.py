# -*- coding: utf-8 -*-
# @Time : 2020/11/27 20:17
# @File : ExcelData.py
# @Author : Yvon_懿払曦

from utils.ExcelUtil import ExcelReader
import json
from common.ExcelConfig import DataConfig

class Data:
    def __init__(self,case_file,sheet_name):
    #1、使用excel工具类，获取结果list
        # self.reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
        self.reader = ExcelReader(case_file, sheet_name)  #文件名、sheet_name参数化
        # print(self.reader.data())

    #2、列是否运行内容，y
    def get_run_data(self):
        """
        根据运行列是否==y,获取测试用例
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            #if line[DataConfig.is_run] == "y":
            if str(line[DataConfig().is_run]).lower() == "y":   #大小写转换Y
                # print(line)
                #print(json.dumps(line, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))  # Json格式打印
                run_list.append(line)
        # print(json.dumps(run_list, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))  # Json格式打印
        return run_list


    def get_case_list(self):
        """
        获取全部的测试用例
        :return:
        """
        #方法一
        # run_list = list()
        # for line in self.reader.data():
        #     run_list.append(line)
        # return  run_list

        # 方法二  列表推导
        run_list = [line for line in self.reader.data()]
        return run_list


    def get_case_pre(self,pre):
        #获取全部测试用例
        #list判断、执行、获取
        """
        根据前置条件:从全部测试用例取到测试用例
        :param pre:
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None


# if __name__ == "__main__":
#     print(Data.get_run_data(self))