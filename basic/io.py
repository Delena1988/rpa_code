# # 读取键盘输入
# str = input("请输入：")
# print("你输入的内容是: ", str)
import os

# 打开一个文件
fo = open("foo.txt", "w")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

fo.write("www.runoob.com!\nVery good site!\n")
# 关闭文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str1 = fo.read(10)
print("读取的字符串是 : ", str1)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str2 = fo.read(10)
print("重新读取字符串 : ", str2)
# 关闭打开的文件
fo.close()

print(os.getcwd())
