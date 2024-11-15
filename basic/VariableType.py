counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter, miles, name)

a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, "john"
print(a, b, c)

print("================字符串================")
str = 'Hello World!'
print("输出完整字符串: ", str)
print("输出字符串中的第一个字符: ", str[0])
print("输出字符串中第三个至第六个之间的字符串: ", str[2:5])
print("输出从第三个字符开始的字符串: ", str[2:])
print("输出字符串两次: ", str * 2)
print("输出连接的字符串: ", str + "TEST")
print("\n")

print("================列表================")
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print("输出完整列表: ", list)
print("输出列表的第一个元素: ", list[0])
print("输出第二个至第三个元素: ", list[1:3])
print("输出从第三个开始至列表末尾的所有元素: ", list[2:])
print("输出列表两次: ", tinylist * 2)
print("打印组合的列表: ", list + tinylist)
print("\n")

print("================元组================")
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print("输出完整元组: ", tuple)
print("输出元组的第一个元素: ", tuple[0])
print("输出第二个至第四个（不包含）的元素: ", tuple[1:3])
print("输出从第三个开始至列表末尾的所有元素: ", tuple[2:])
print("输出元组两次: ", tinytuple * 2)
print("打印组合的元组", tuple + tinytuple)
print("\n")

print("================字典================")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print("输出键为'one' 的值: ", dict['one'])
print("输出键为 2 的值: ", dict[2])
print("输出完整的字典: ", tinydict)
print("输出所有键: ", tinydict.keys())
print("输出所有值: ", tinydict.values())
print("\n")
