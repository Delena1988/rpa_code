# 02-print 函数
print('hello world!')
print('hello', 'world!')  # 逗号自动添加默认的分隔符：空格 hello world!
print('hello' + 'world!')  # 加号表示字符拼接 helloworld!
print('hello', 'world', sep='***')  # 单词间用***分隔 hello***world
print('#' * 50)  # *号表示重复 50 遍
print('how are you?', end='')  # 默认 print 会打印回车，end=''表示不要回车
print()
print("this ""is ""string")