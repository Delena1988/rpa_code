print("===================算数运算符===================")
a = 21
b = 10
c = 0

c = a + b
print(a, "+", b, "的值为：", c)
c = a - b
print(a, "-", b, "的值为：", c)
c = a * b
print(a, "*", b, "的值为：", c)
c = a / b
print(a, "/", b, "的值为：", c)
c = a % b
print(a, "%", b, "的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
# 幂 - 返回x的y次幂
c = a ** b
print(a, "**", b, "的值为：", c)
a = 10
b = 5
# 取整除 - 返回商的整数部分（向下取整）
c = a // b
print(a, "//", b, "的值为：", c)
print("\n")

print("===================比较运算符===================")
a = 21
b = 10
c = 0
if a == b:
    print("a 等于 b")
else:
    print("a 不等于 b")

if a != b:
    print("a 不等于 b")
else:
    print("a 等于 b")

if a < b:
    print("a 小于 b")
else:
    print("a 大于等于 b")

if a > b:
    print("a 大于 b")
else:
    print("a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("a 小于等于 b")
else:
    print("a 大于  b")

if b >= a:
    print("b 大于等于 a")
else:
    print("b 小于 a")
print("\n")

print("===================位运算符===================")
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print(a, "&", b, "的值为：", c)

c = a | b;  # 61 = 0011 1101
print(a, "|", b, "的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print(a, "^", b, "的值为：", c)

c = ~a;  # -61 = 1100 0011
print("~", a, "的值为：", c)

c = a << 2;  # 240 = 1111 0000
print(a, "<<", 2, "的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print(a, ">>", 2, "的值为：", c)
