# -*- coding: utf-8 -*-
# @Time    : 2023/3/13 12:39
# @Author  : YZN
# @File    : test_addStep.py
# @Description : 新增步骤
import allure

import pytest
from api.api import addStep
from testcases.testTicketTable.conftest import get_task_id, test

@allure.epic("iphmart项目")
@allure.feature("典操表功能")
#设置用例的执行顺序
@pytest.mark.run(order=3)
class TestStep:
    @allure.story('新增活动下的步骤')
    @allure.title("正常新增典操表API闵行开发区停役p的活动步骤")
    @allure.testcase('http://www.baidu.com', name='用例地址')
    @allure.issue('http://www.baidu.com', name='缺陷地址')
    @allure.link('http://www.baidu.com', name='链接地址link')
    @allure.description('根据新增的API闵行开发区停役典操表，在下面新增活动下的步骤')
    @allure.step('新增活动下面的步骤')
    @allure.severity("blocker")
    def test_add_step(self,login_fixture):
        token = login_fixture
        #拿到查出的tableid
        #tableid = gettask.test_add_task(login_fixture)ytet
        #tableid = test_add_task(test_add_table(login_fixture))
        #tableid = os.environ['tableid']
        #取出字典表id赋值
        tableid=test.tableid
        print('hhhhhhhhhhhhhhhhhhhhh'+str(tableid))
        # 通过字典表id查出任务id和code
        task_id = get_task_id(tableid)
        i=0
        #通过for循环取出两组新增的任务id和code,在每个任务下新增步骤
        for a in task_id:
            print(a['id'])
            for i in range(0,1):
                result=addStep(tableid,a['id'],a['code'],token)
                print(result.body)
                assert result.success is True
                assert result.body['msg']=="操作成功"
                i=+1


