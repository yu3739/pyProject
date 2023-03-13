
import json

import requests

from utils.log_util import logger
from utils.read_data import get_data

api_54_url = get_data.read_ini()['host']['54_url']
api_56_url = get_data.read_ini()['host']['56_url']


print(api_54_url)


class RestClient:
    def __init__(self):
        self.api_root_url=api_54_url

    # C方法
    def get(self, path, **kwargs):
        return self.request(path, "get", **kwargs)

    # C方法
    def post(self, path, **kwargs):

        return self.request(path, "post", **kwargs)

    def put(self, path, **kwargs):
        return self.request(path, "put", **kwargs)

    def delete(self, path, **kwargs):
        return self.request(path, "delete", **kwargs)

    def request(self, path, method, **kwargs):
        self.request_log(path, method, **kwargs)

        if method == "get":
            return requests.get(self.api_root_url + path, **kwargs)
        if method == "post":
            return requests.post(self.api_root_url + path, **kwargs)
        if method == "put":
            return requests.put(self.api_root_url + path, **kwargs)
        if method == "delete":
            return requests.delete(self.api_root_url + path, **kwargs)

    def request_log(self, path, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")
        logger.info("接口请求的地址>>>{}".format(self.api_root_url + path))
        logger.info("接口请求的方法>>>{}".format(method))
        if data is not None:
            logger.info("接口请求的参数>>>\n{}".format(json.dumps(data, indent=2,ensure_ascii=False)))
        if json_data is not None:
            logger.info("接口请求的参数>>>\n{}".format(json.dumps(json_data, indent=2,ensure_ascii=False)))
        if params is not None:
            logger.info("接口请求的参数>>>\n{}".format(json.dumps(params, indent=2,ensure_ascii=False),))
        if headers is not None:
            logger.info("接口请求头的参数>>>\n{}".format(json.dumps(headers, indent=2,ensure_ascii=False)))

