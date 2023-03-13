# # -*- coding: utf-8 -*-
# # @Time    : 2023/3/10 15:30
# # @Author  : YZN
# # @File    : test_addTask.py
# # @Description :新增典操表下的活动
# import allure
# import requests
# import pytest
#
# from api.api import addTable
# from utils.read_data import get_data
# from utils.yaml_util import func_yaml
#
#
# @allure.epic("iphmart项目")
# @allure.feature("典操表功能")
#
# class TestLogin:
#     @allure.story('新增典操表下的活动')
#     @allure.title("正常新增典操表API闵行开发区停役下的活动")
#     @allure.testcase('http://www.baidu.com', name='用例地址')
#     @allure.issue('http://www.baidu.com', name='缺陷地址')
#     @allure.link('http://www.baidu.com', name='链接地址link')
#     @allure.description('根据新增的API闵行开发区停役典操表，在下面新增活动')
#     @allure.step('新增典操表下面的活动')
#     @allure.severity("blocker")
#     def test_add_task(self,login_fixture):
#         token = login_fixture
#         json_data=get_data.read_data()['taskyaml']['json_data']
#
#         result=addtask(func_yaml(json_data),token)
#         #r = requests.post('http://10.89.33.54:3001/mro/ticketClassicOperationTable/table', json= json_data, headers=headers)
#         print(result.body)
#         assert result.success is True
#         assert result.body['msg']=="操作成功"
# import os


# def test1():
#
#     #print(vvv.test_add_table())
#     print("======"+os.environ['b'])
#     # aa=os.environ['b']
#     # return aa