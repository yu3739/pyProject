#处理yaml自定义函数的配置
import random
#引入Faker工具
from faker import Faker
#初始化，设置locale为中文；默认是英文
fake=Faker(locale='zh-CN')
def func_yaml(data):
    #isinstance用来判断元素类型,如果传入的data是字典类型
    if isinstance(data,dict):
        #获取字典的key,value
        for key,value in data.items():
            # 如果yaml参数文件里的value有random,要转成字符串
            if '${'and'}'in str(value):
                #取出前面的部分和后面的部分
                start=str(value).index('${')
                end=str(value).index('}')
                #拼切片的方式拼起来
                func_name=str(value)[start+2:end]
                #重新赋值，eval里面必须是字符串；设置可以在$符号前拼上其他的字符串内容固定值+随机值，从0开始加上$后面的内容
                #只能拼字符串
                #data[key]=str(value)[0:start]+eval(func_name)

                #把int的值也可以拼，但是原本的int参数也会变成str
                #data[key]=str(value)[0:start]+str(eval(func_name))
                #在自定义的前面和后面都可以拼固定参数
                #data[key]=str(value)[0:start]+str(eval(func_name))+str(value)[end+1:len(str(value))]

                # 在自定义的前面和后面都可以拼固定参数，但是固定入参只能是字符串
                #data[key]=str(value)[0:start]+eval(func_name)+str(value)[end+1:len(str(value))]

                #如果前后拼的是空字符串，就不转str，保持原本入参的数据类型，但是不能拼前后的参数
                if str(value)[0:start]=='' and str(value)[end+1:len(str(value))]=='':
                    data[key] = eval(func_name)
                    #否则可以拼前后的参数，但是整个入参都必须是str类型
                else:
                    data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end + 1:len(str(value))]
                    #上面的if语句可以给str拼接又不改变int的数据类型。不能做int的拼接只能做str拼接。如果给int拼接就会变成str。

    return data
def random_name():
    #返回一个随机的姓名/
    return fake.name()
def random_week():
    #返回随机星期数
    return  fake.day_of_week()
    #返回时间戳
def random_unix_time():

    return fake.unix_time()

#yaml文件参数被引入的参数名
def age():
    #把固定数字和随机数字拼接
    b='156'+str(random.randint(10,100))
    return int(b)
    #直接返回随机int数字
    #return (random.randint(10,100))

if __name__ == '__main__':
    data={'name': '${random_name()}', 'age': '${age()}', 'sex': '男'}
    print(func_yaml(data))