#pymysql_eg.py
import pymysql
conn = pymysql.connect(host="localhost",#MySQL服务端地址
                       user="root",     #登录MySQl的用户名
                       password="123456",     #密码
                       db="hero"）       #要连接的库名

cur = conn.cursor()     #创建游标
sqlCT = "create table player (name VARCHAR(30), age INT,sex CHAR(1))"
cur.execute(sqlCT)    #创建表
                       
cur.execute("insert into player VALUES ('milo', 18, 'M')")
cur.execute("insert into player VALUES ('zou', 20, 'M')")
cur.execute("insert into player VALUES ('qi', 21, 'F')")
cur.execute("insert into player VALUES ('xian', 21, 'F')")
conn.commit()       #事务提交

cur.execute("update player set age=19 where name='milo'")  #修改数据
cur.execute("delete from player where name='zou'")  #删除数据
cur.execute("select * from player") #执行查询命令

one = cur.fetchone()    #获得一条数据
all = cur.fetchall()    #获得多条数据
print(one)
print(all)

cur.close()     #关闭游标
conn.close()    #关闭数据库连接
