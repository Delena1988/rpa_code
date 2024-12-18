import sqlite3

# 创建连接
conn = sqlite3.connect('students.db')
# 游标
c = conn.cursor()
# 插入单条数据
sql = """update students set age = ? where name = ?  """
params = (24, 'john',)
c.execute(sql, params)
# 执行
conn.commit()
# 关闭连接
conn.close()
