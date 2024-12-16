import sqlite3

# 创建连接
conn = sqlite3.connect('students.db')
# 游标
c = conn.cursor()
# 插入多条数据
all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7),
    ('michael', 19, 1.83),
]
c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)
# 执行
conn.commit()
# 关闭连接
conn.close()
