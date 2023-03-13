import os

import allure
import pytest

from api.api import addTable
from utils.read_data import get_data
from utils.yaml_util import func_yaml


@allure.epic("iphmart项目")
@allure.feature("典操表功能")

class TestTable:
    @allure.story('新增典操表')
    @allure.title("正常新增典操表")
    @allure.testcase('http://www.baidu.com', name='用例地址')
    @allure.issue('http://www.baidu.com', name='缺陷地址')
    @allure.link('http://www.baidu.com', name='链接地址link')
    @allure.description('对用例的详细描述写这里description')
    @allure.step('先新增一个典操表')
    @allure.severity("blocker")
    def test_add_table(self,login_fixture):
        token = login_fixture
        json_data=get_data.read_data()['tableyaml']['json_data']
        a=func_yaml(json_data)
        print("----------"+str(a))
        #os.environ['b']=str(a['name'])
        # print('======='+b)
        b=a['name']
        result=addTable(a,token)
        print(result.body)
        assert result.success is True
        assert result.body['msg']=="操作成功"
        return b

vvv=TestTable()











