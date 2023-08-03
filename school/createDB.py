import sqlite3

conn = sqlite3.connect('school.db')
print("数据库打开成功")
c = conn.cursor()
c.execute('''CREATE TABLE school
       (ID INT PRIMARY KEY NOT NULL, 
        SCHOOL_NAME VARCHAR(30) NOT NULL, -- 学校名称
        SCHOOL_ABBR VARCHAR(10) NOT NULL -- 学校简称
        );''')

c.execute('''CREATE TABLE student
       (ID INT PRIMARY KEY NOT NULL,
        STUDENT_NAME VARCHAR(30) NOT NULL,-- 学生姓名
        SEX_CODE INTEGER NOT NULL, -- 性别代码
        SEX_NAME VARCHAR(10) NOT NULL -- 性别名称
        );''')
print("数据表创建成功")
conn.commit()
conn.close()
