# -*- coding: utf-8 -*-
# @Time : 2020/12/2 11:21
# @File : test_excel_case.py
# @Author : Yvon_₯㎕ζ๓

from config.Conf import ConfigYaml
from common.ExcelData import Data
from utils.LogUtil import my_log
from common.ExcelConfig import DataConfig
from utils.RequestsUtil import Request
import os,json,pytest


#1、初始化信息
#1).初始化测试用例文件
case_file = os.path.join("../data",ConfigYaml().get_excel_file()) # 拼接路径+文件
# print(case_file)
#2).测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# print(sheet_name)
#3).获取运行测试用例列表
run_list = Data(case_file,sheet_name).get_run_data()
# print(json.dumps(run_list, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))  # Json格式打印

#4).日志
log = my_log()
#2、测试用例方法、参数化运行
#先用一个用例去调试
class TestExcel:
#1).初始化信息url,data
    #1、增加pytest
    @pytest.mark.parametrize("case",run_list)
    #2、修改方法参数
    def test_run(self,case ):
        data_key = DataConfig()
        #run_list 第一个用例,用例,key获取values
        url = ConfigYaml().get_conf_url() + case[data_key.url]
        print(url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]

        #判断headers是否存在，json转义，无需
        if headers:
            header = json.loads(headers)
        else:
            header = headers

        #判断cookies是否存在，json转义，无需
        if cookies:
            cookie = json.loads(cookies)
        else:
            cookie = cookies


        # 接口请求
        request = Request()
        # params 转义json
        #验证params 有没有内容
        if len(str(params).strip()) != 0:
            params = json.loads(params)
        #method post/get
        if str(method).lower()=="get":
            #增加headers,cookies
            res = request.get(url,json = params,headers = header,cookies = cookie)
        elif str(method).lower()=="post":
            res = request.post(url, json=params,headers = header,cookies = cookie)
        else:
            log.error("错误请求method: %S"%method)
        print(res)

if __name__ == "__main__":
    # TestExcel().test_run()
    pytest.main(["-s","test_excel_case.py"])




"""
#固定headers请求
    #1.判断headers是否存在，json转义，无需
    #2.增加Headers
    #3.增加cookies
    #4.发送请求

"""