# -*- coding: utf-8 -*-
# @Time : 2020/12/2 11:21
# @File : test_excel_case.py
# @Author : Yvon_₯㎕ζ๓

from config.Conf import ConfigYaml
from common.ExcelData import Data
from common.ExcelConfig import DataConfig
from common import Base
from config import Conf
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
import os,json,pytest
import allure


#1、初始化信息
#1).初始化测试用例文件
case_file = os.path.join(Conf.get_data_path(),ConfigYaml().get_excel_file()) # 拼接路径+文件
# print(case_file)
#2).测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
print(sheet_name)
#3).获取运行测试用例列表
data_init = Data(case_file,sheet_name)
run_list = data_init.get_run_data()
# print(json.dumps(run_list, sort_keys=True, ensure_ascii=False, indent=4, separators=(', ', ': ')))  # Json格式打印

#4).日志
log = my_log()

#初始化DataConfig
data_key = DataConfig()
#2、测试用例方法、参数化运行
#先用一个用例去调试

class TestExcel:

    def run_api(self,url,method,params=None,header=None,cookie=None,):

        """
        发送请求api
        :return:
        """
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
            log.error("错误请求method: %S"% method)
        # print(res)
        return res


    def run_pre(self,pre_case):

        """
        前置条件运行
        :param pre_case:
        :return:
        """
        pass
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]

        header = Base.json_parse(headers)
        cookie = Base.json_parse(cookies)
        res = self.run_api(url,method,params,header)
        print("前置用例执行: %s"%res)
        return res

#1).初始化信息url,data
    #1、增加pytest
    @pytest.mark.parametrize("case",run_list)
    #2、修改方法参数
    def test_run(self,case):

        #run_list 第一个用例,用例,key获取values
        url = ConfigYaml().get_conf_url() +case[data_key.url]
        print(url)
        case_id = case[data_key.case_id]
        # print(case_id)
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


        #动态headers请求
        ##1.验证前置条件
        if pre_exec:
            pass

        ##2.找到执行用例
            pre_case = data_init.get_case_pre(pre_exec)

            print("前置条件信息为: %s" %pre_case)
            pre_res = self.run_pre(pre_case)
            headers,cookies = self.get_correlation(headers,cookies,pre_res)

        header = Base.json_parse(headers)
        cookie = Base.json_parse(cookies)
        res = self.run_api(url, method, params, header, cookie)
        print("测试用例执行: %s" % res)
        # return res  # 注意

        # sheet名称--feature 一级标签
        allure.dynamic.feature(sheet_name)
        # 模块--story 二级标签
        allure.dynamic.story(case_model)
        # 用例ID + 接口名称 - - title
        allure.dynamic.title(case_id+case_name)
        #请求URL 请求类型 期望结果 实际结果 description
        # allure.dynamic.description(url+method+expect_result+res)
        desc = "<font color='green' size=3>请求URL: </font> {}<Br/>" \
               "<font color='green' size=3>请求类型: </font>{}<Br/>" \
               "<font color='red' size=3>期望结果: </font>{}<Br/>" \
               "<font color='green' size=3>实际结果: </font>{}".format(url, method, expect_result, res)
        allure.dynamic.description(desc)



        #1.断言验证
        #2.状态码，返回结果内容，数据库相关结果验证
        #"""断言验证--状态码，返回结果内容，数据库相关的结果的验证"""
        #1.)状态码
        assert_util = AssertUtil()
        assert_util.assert_code(int(res["code"]),int(code))
        #2.)返回结果内容验证
        assert_util.assert_in_body(str(res["body"]),str(expect_result))
        #********数据库结果断言********
        Base.assert_db("db_1",res["body"],db_verify)


    def get_correlation(self,headers,cookies,pre_res):
        """
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        #验证是否有关联
        headers_para,cookies_para = Base.params_find(headers,cookies)
        #有关联,执行前置用例,获取结果
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
        #结果替换
            headers = Base.res_sub(headers,headers_data)

        #有关联,执行前置用例,获取结果
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
        #结果替换
            cookies = Base.res_sub(headers,cookies_data)

        return headers, cookies



if __name__ == "__main__":
    # pass
    # TestExcel().test_run()
    # pytest.main(["-s","test_excel_case.py"])
    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"

    pytest.main(["-s", "test_excel_case.py", "--alluredir", report_path ])
    Base.allure_report(report_path, report_html_path)
    Base.send_mail(title="接口测试报告结果", content=report_html_path)






#动态headers请求
    #1.验证前置条件
    #2.找到执行用例
    #3.发送请求，获取前置用例结果
        #发送获取前置测试用例，用例结果
        #数据初始化，get/post，重构
    #4.替换Headers变量
        #1.验证请求中是否${}$,返回${}$内容
    # str1 = '{"Authorization": "JWT ${token}$"}'
    # if '${' in str1:
    #     print(str1)
    # import re
    # pattern = re.compile('\${(.*)}\$')
    # re_res = pattern.findall(str1)
    # print(re_res)
    # print(re_res[0])
    #     #2.根据内容token,查询前置条件测试用例返回结果token = 值
    # token = '123'
    #     #3.根据变量结果内容,替换
    # res = re.sub(pattern,token,str1)
    # print(res)
    #5.请求发送

    #1、查询，公共方法
    #2、替换，公共方法
    #3、验证请求中是否${}$，返回${}$内容，公共方法
    #4、关联方法