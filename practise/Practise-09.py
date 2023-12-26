# 09-字典基础
# 字典是 key-value（键－值）对形式的，没有顺序，通过键取出值
adict = {'name': 'bob', 'age': 23}
len(adict)
'bob' in adict  # False
'name' in adict  # True
adict['email'] = 'bob@tedu.cn'  # 字典中没有 key，则添加新项目
adict['age'] = 25  # 字典中已有 key，修改对应的 value


