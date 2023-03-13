
import os

import allure
import pytest
from api.api import login
from testcases.testTicketTable.test_addTable import TestTable
#from utils.mysql_utils import db
from utils.read_data import get_data

@pytest.fixture  #每个用例执行前都会执行一次这个方法，如果引用过的话
@allure.step('先登录获取token')
def login_fixture():
    if 'token' not in os.environ:
        data=get_data.read_data()['login']['json_data']
        # password=data['password']
        # mobile=data['mobile']
        #执行登录接口
        result=login(data)
        #把token存进环境变量
        os.environ['token']=result.body['data']['access_token']

        # #环境变量存进去必须是str
        # os.environ['mobile']=str(mobile)
        return result.body['data']['access_token']

    else:
        return os.environ['token']





#from utils.mysql_utils import db
# a=TestTable()
# print("======" + a.test_add_table())

def test_a():
    a=TestTable.test_add_table()
    print('dffdfdffdfdfdfdf'+a)

