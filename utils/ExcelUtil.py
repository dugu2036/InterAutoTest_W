# -*- coding: utf-8 -*-
# @Time : 2020/11/26 17:43
# @File : ExcelUtil.py
# @Author : Yvon_懿払曦

import os
import xlrd ,json


#目的：参数化，pytest list文件形式读取
# 自定义异常
class SheetTypeError:
    pass
#1、验证文件是否存在，存在读取，不存在报错
class ExcelReader:
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("文件不存在")


#2、读取sheet方式.名称,索引
    def data(self):
        # 存在不读取，不存在读取
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by)  not in [str,int]:

                raise SheetTypeError("请输入int or str")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)  # int型
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)  # str型

    #3、sheet内容
            # 返回list,元素:字典
            #格式[{'company': '可口可乐', 'manager': 'Shirley'}, {'company': '北极光', 'manager': 'marry'}]
            #1.获取首行信息
            title = sheet.row_values(0)
            #2.遍历测试行,与首行组成dict,放在list
                #1.循环,过滤首行,从1开始
            for col in range(1,sheet.nrows):
                col_value = sheet.row_values(col)
                #2.与首行组成字典,放list
                self._data.append(dict(zip(title, col_value)))

#4、返回结果
        return self._data

"""
# 参考实例
head = ["company","manager"]
value1 = ["可口可乐","Shirley"]
value2 = ["北极光","marry"]
# print(dict(zip(head,value1)))
# print(dict(zip(head,value2)))
data_list = list()
data_list.append(dict(zip(head,value1)))
data_list.append(dict(zip(head,value2)))
print(data_list)
"""
if __name__ == "__main__":
    reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
    result = reader.data()
    # print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))  # Json格式打印


