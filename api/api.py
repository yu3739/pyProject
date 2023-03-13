import json

from core.api_util import api_util
#from utils.log_util import logger
#from utils.response_util import process_response

from utils.read_data import get_data
from utils.response_util import process_response

#A方法
def login(json_data):
    """
    登录接口入参
    :param json_data:json入参
    :return:接口请求的结果，放在body里
    """
    # 调B方法
    #headers = get_data.read_data()['login']

    response = api_util.login(json=json_data)
    # 调用方法打印接口返回的日志
    result=process_response(response)

    #response = api_util.post_data(json_data=json_data)
   # return result
    return result
#A方法
def addTable(json_data,token):
    """
    新增典操表，json传参数
    :param json_data:json入参
    :return:接口请求的结果，放在body里
    """
    # 调B方法
    # headers = get_data.read_data()['table']['Authorization']
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = api_util.addTable_data(json=json_data,headers=headers)
    # 调用方法打印接口返回的日志
    result=process_response(response)

    #response = api_util.post_data(json_data=json_data)
   # return result
    return result

def addTask(json_data,token):
    """
    新增典操表任务，json传参数
    :param json_data:json入参
    :return:接口请求的结果，放在body里
    """
    # 调B方法
    # headers = get_data.read_data()['table']['Authorization']
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = api_util.addTask_data(json=json_data,headers=headers)
    # 调用方法打印接口返回的日志
    result=process_response(response)

    #response = api_util.post_data(json_data=json_data)
   # return result
    return result