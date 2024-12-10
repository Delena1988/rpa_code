import sqlite3

# 创建连接
conn = sqlite3.connect('students.db')
# 游标
c = conn.cursor()
# 建表语句
c.execute("""CREATE TABLE students (
            name TEXT,
            age INTEGER,
            height REAL
    )""")
# 执行
conn.commit()
# 关闭连接
conn.close()
