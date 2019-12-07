import pymysql


# 用来操作数据库的类
class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "123456"  # 密码
        self.db = "th"  # 库
        self.table = "th"  # 表

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
            print("连接成功")
        except:
            print('connect mysql error.')

    # 查询数据
    def queryMysql(self,keyword,type):
        sql = "SELECT * FROM " + self.table + " WHERE (title LIKE'%" + keyword + "%' OR content LIKE '%" + keyword + "%')"
        if not type:
            sql=sql
        else:
            sql=sql+" AND type='"+type+"'"
        th_list=[]
        print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                #print(row)
                th_list.append(row)
            #print(keyword)
            print("查询成功")
            return th_list
        except:
            print(sql + ' execute failed.')

    # 插入数据
    def insertMysql(self, id, type,title, href,time,content):
        sql = "INSERT INTO " + self.table + " VALUES(" + id + "," + "'" + type + "',"+ "'" + title + "'," + "'" + href +"',"+"'"+time+"',"+"'"+content+ "')"
        try:
            self.cursor.execute(sql)
            self.conn.commit()

        except:
            print( id)
            print(sql)
            print("insert failed.")
            print("----------------")

    # 更新数据
    def updateMysqlSN(self, title, href):
        sql = "UPDATE " + self.table + " SET href='" + href + "'" + " WHERE title='" + title + "'"
        print("update sn:" + sql)
        self.conn.commit()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()
