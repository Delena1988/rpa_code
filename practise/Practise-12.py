# 12-判断练习：用户名和密码是否正确
import getpass  # 导入模块

username = input('username: ')
# getpass 模块中，有一个方法也叫 getpass
password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('Login successful')
else:
    print('Login incorrect')





