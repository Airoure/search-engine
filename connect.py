# coding=utf-8
import pymysql
coon = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = '123456', port = 3306, db = 'mysql', charset = 'utf8')
cur = coon.cursor()
cur.execute("select * from 学生")
num = cur.execute("select * from 学生")
i: int
for i in range(num):
    res = cur.fetchone()
    print(res)
# print(res)
cur.close()
coon.close()

