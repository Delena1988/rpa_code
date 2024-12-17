import sqlite3

# 创建连接
conn = sqlite3.connect('students.db')
# 游标
c = conn.cursor()
# 查询数据
c.execute("SELECT * FROM students")
print(c.fetchone())
# 执行
conn.commit()
# 关闭连接
conn.close()
