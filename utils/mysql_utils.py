import pymysql

from utils.log_util import logger
from utils.read_data import get_data
#获取写在setting.ini文件里面的数据库链接数据
data=get_data.read_ini()['mysqliphmart-mro']
#组装数据库链接的数据
DB_conf={
    "host":data['mysql_host'],
    #port转成int类型
    "port":int(data['mysql_port']),
    "user":data['mysql_user'],
    "password":data['mysql_password'],
    "db":data['mysql_db']
}

class MysqlDB:

    def __init__(self):
        #mysql连接，**代表去组装数据里拿参数，是否主动提交=是
        self.conn=pymysql.connect(**DB_conf,autocommit=True)
        #创建游标，有游标才能进行数据库操作
        self.cur=self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    #释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    #单独做一个select方法 ，查询一条数据
    def select_db_one(self,sql):
        """
        select查询一条数据
        @param sql:
        @return:
        """
        logger.info(f'执行sql:{sql}')
        #用execute执行sql
        self.cur.execute(sql)
        #获取结果
        result =self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        #获取一条数据
        return result

    # 单独做一个select方法 ，查询多条数据
    def select_db_all(self,sql):
        """
        select查询多条数据
        :param sql:
        :return:
        """
        logger.info(f'执行sql:{sql}')
        self.cur.execute(sql)
        result = self.cur.fetchall()
        logger.info(f'sql执行结果：{result}')
        # 获取多条数据
        return result
    #更新数据
    def execute_db(self,sql):
        """
        更新数据
        :param sql:
        """
        #当执行sql报错抛出异常
        try:
            #打印执行的sql
            logger.info(f'执行sql:{sql}')
            #执行sql
            self.cur.execute(sql)
            #提交sql
            self.conn.commit()
        #异常捕获
        except Exception as e:
            logger.info("执行sql出错{}".format(e))
db=MysqlDB()
if __name__ == '__main__':
    db=MysqlDB()
    result=db.select_db_all("SELECT id,code from ticket_classic_operation_table_task where table_id=193 order by id desc")
    #查出字典数组
    print(result[0]['id'])