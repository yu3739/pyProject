# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 15:30
# @Author  : YZN
# @File    : test_addTask.py
# @Description :新增典操表下的活动
import os
from itertools import count

import allure
import requests
import pytest

from api.api import addTask
from testcases.testTicketTable.conftest import get_id, test
from testcases.testTicketTable.test_addTable import gettable



@allure.epic("iphmart项目")
@allure.feature("典操表功能")
#设置用例的执行顺序
@pytest.mark.run(order=2)
class TestTask:
    @allure.story('新增典操表下的活动')
    @allure.title("正常新增典操表API闵行开发区停役下的活动")
    @allure.testcase('http://www.baidu.com', name='用例地址')
    @allure.issue('http://www.baidu.com', name='缺陷地址')
    @allure.link('http://www.baidu.com', name='链接地址link')
    @allure.description('根据新增的API闵行开发区停役典操表，在下面新增活动')
    @allure.step('新增典操表下面的活动')
    @allure.severity("blocker")

    def test_add_task(self,login_fixture):
        token = login_fixture
        #name=gettable.test_add_table(login_fixture)
        #name=test_add_table(login_fixture)

        #从那个单独的文件里取出参数
        name=test.tablename
        print('fffffffffff'+name)
        # 通过取出的典操表名称在数据库查出典操id
        tableid = str(get_id(name)['id'])
        #tableid = str(get_id(os.environ['tablename'])['id'])
        #把任务id设置成环境变量
         #os.environ['tableid']=tableid

        # 把典操表id参数单独放在一个文件里存着
        test.tableid=tableid
        print('ggggggggggggggggggggg'+test.tableid)
        i=0
        for i in range(0,2):
            result=addTask(tableid,token)
            print(result.body)
            assert result.success is True
            assert result.body['msg']=="操作成功"
            i=+1
        return test.tableid

gettask=TestTask()
