import configparser
import os
import yaml
#读取data文件和ini路径和内容
data_path=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'data','data.yaml')
print(data_path)
# 拿到路径，读取settings.ini文件的域名配置   #读取ini文件
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', 'settings.ini')
class FileRead:
    def __init__(self):
        self.data_path=data_path
        self.ini_path=ini_path
    def read_data(self):
        """
        读取data.yaml文件里参数的方法
        :return:字典格式
        """
        f=open(self.data_path,encoding='utf8')
        #用yaml的一个方法读取f这个文件的内容
        data=yaml.safe_load(f)
        #print(data['table'])
        return data

    def read_ini(self):
        """
        读取setting.ini文件里的内容
        :return:字典取值
        """
        # 用configparser工具读取ini文件的配置内容
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config

get_data=FileRead()
print(get_data.read_data())
print(get_data.read_ini()['host']['54_url'])
print(get_data.read_data()['login']['json_data'])