c = set(("a", "b", "c"))
d = list(c)

print(c)
print(d)

a = [1, 2, 3]
b = [1, 2, 6, 9, 12]
print(set(a) & set(b))  # 交集
print(set(a) | set(b))  # 并集
print(set(a) ^ set(b))  # 异或，就是两个集合去掉交集的那部分
print(set(a) - set(b))  # 差集，就是a去掉b中元素剩下的那部分
