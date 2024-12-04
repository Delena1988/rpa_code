import psycopg2

# 方式1
# 获得连接
conn = psycopg2.connect(database="python", user="postgres", password="123456", host="127.0.0.1", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql = "INSERT INTO student (num, name) \
                    VALUES (%s, '%s')" % \
      (100, 'zszxz')
# 执行语句
cursor.execute(sql)
print("successfully")
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()


# 方式2
# 获得连接
conn = psycopg2.connect(database="python", user="postgres", password="123456", host="127.0.0.1", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql = """INSERT INTO student (num, name) VALUES (%s, %s)"""
params = (101, 'zszxz')
# 执行语句
cursor.execute(sql, params)
print("successfully")
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()

# 方式3
# 获得连接
conn = psycopg2.connect(database="python", user="postgres", password="123456", host="127.0.0.1", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cursor = conn.cursor()
# sql语句 建表
sql = """INSERT INTO student (num, name) VALUES (%(num)s, %(name)s)"""
params = {'num': 102, 'name': 'zszxz'}
# 执行语句
cursor.execute(sql, params)
print("successfully")
# 事物提交
conn.commit()
# 关闭数据库连接
conn.close()
