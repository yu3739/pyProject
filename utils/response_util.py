import json

from core.ResultBase import ResultResponse
from utils.log_util import logger


#统一打印接口返回的日志内容,返回json体
def process_response(response):

    if response.status_code==200 or response.status_code==201:
        ResultResponse.success=True
        logger.info('接口返回的内容>>>: ' + json.dumps(response.json(), ensure_ascii=False))
        ResultResponse.body=response.json()
    else:
        ResultResponse.success = False
        logger.info("接口状态码不是2开头，请检查")
    #如果返回码不是2开头的也打印接口返回内容
        logger.info('接口返回的内容>>>: ' + json.dumps(response.json(), ensure_ascii=False))

    return ResultResponse