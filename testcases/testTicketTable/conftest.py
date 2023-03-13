# -*- coding: utf-8 -*-
# @Time    : 2023/3/13 9:37
# @Author  : YZN
# @File    : conftest.py
# @Description :
import os

import allure

from utils.log_util import logger
from utils.mysql_utils import db

@allure.step('用典操表名称获取典操表的id')
def get_id(name):

    sql="select id from ticket_classic_operation_table where name='%s' order by id desc"%name
    result=db.select_db_one(sql)
    #print(result)
    #logger.info(f'sql执行结果，{result}')
    return result
    # a=TestTable.test_add_table()
    # print('dffdfdffdfdfdfdf'+a)

@allure.step('用table_id获取task的id')
def get_task_id(table_id):

    sql="select id,code from ticket_classic_operation_table_task where table_id='%s'"%table_id
    #sql="select id,code from ticket_classic_operation_table_task where table_id='%s' order by id desc"%table_id
    result=db.select_db_all(sql)
    print(result)
    #logger.info(f'sql执行结果，{result}')
    return result


class test:
    tablename=None
    tableid=None