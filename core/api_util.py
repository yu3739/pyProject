from core.rest_client import  RestClient

#B方法
class api_util(RestClient):
    def __init__(self):
        super().__init__()

    def login(self,**kwargs):
        """
        登录接口写入path
        :param kwargs:
        :return:
        """
        #新增典操表
        return self.post('/auth/login',**kwargs)

    def addTable_data(self,**kwargs):
        """
        新增典操表写入path
        :param kwargs:
        :return:
        """
        #新增典操表
        return self.post('/mro/ticketClassicOperationTable/table',**kwargs)

    def addTask_data(self,**kwargs):
        """
        新增典操表任务写入path
        :param kwargs:
        :return:
        """
        #新增典操表
        return self.post('/mro/ticketClassicOperationTable/task',**kwargs)


#初始化类，别的文件可用
api_util=api_util()
