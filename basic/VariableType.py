counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)
print("\n")

a = b = c = 1
print(a)
print(b)
print(c)
print("\n")

a, b, c = 1, 2, "john"
print(a)
print(b)
print(c)
print("\n")

print("================字符串================")
str = 'Hello World!'
print("输出完整字符串: " + str)
print("输出字符串中的第一个字符: " + str[0])
print("输出字符串中第三个至第六个之间的字符串: " + str[2:5])
print("输出从第三个字符开始的字符串: " + str[2:])
print("输出字符串两次: " + str * 2)
print("输出连接的字符串: " + str + "TEST")
print("\n")

print("================列表================")
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print("输出完整列表: ")
print(list)
print("输出列表的第一个元素: ")
print(list[0])
print("输出第二个至第三个元素: ")
print(list[1:3])
print("输出从第三个开始至列表末尾的所有元素: ")
print( list[2:])
print("输出列表两次: ")
print(tinylist * 2)
print("打印组合的列表: ")
print(list + tinylist)
print("\n")

print("================元组================")
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print("输出完整元组: ")
print(tuple)
print("输出元组的第一个元素: ")
print(tuple[0])
print("输出第二个至第四个（不包含）的元素: ")
print(tuple[1:3])
print("输出从第三个开始至列表末尾的所有元素: ")
print(tuple[2:])
print("输出元组两次: ")
print(tinytuple * 2)
print("打印组合的元组")
print(tuple + tinytuple)
print("\n")

print("================字典================")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print("输出键为'one' 的值: ")
print(dict['one'])
print("输出键为 2 的值: ")
print(dict[2])
print("输出完整的字典: ")
print(tinydict)
print("输出所有键: ")
print(tinydict.keys())
print("输出所有值: ")
print(tinydict.values())
print("\n")