import sqlite3

# 创建连接
conn = sqlite3.connect('students.db')
# 游标
c = conn.cursor()
# 插入单条数据
c.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")
# 执行
conn.commit()
# 关闭连接
conn.close()
