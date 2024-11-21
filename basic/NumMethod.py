import math
import operator
import string

# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
print(abs(-10))
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
print(math.ceil(4.2))
# operator.gt(x, y)	如果 x > y 返回 True 如果x <= y 返回 False
print(operator.gt(10, 15))
print(operator.lt(10, 15))
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
print(math.floor(4.9))
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print(math.log(math.e))
print(math.log(100, 10))
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
print(math.log10(100))
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
print(max(2, 5, 9, 4))
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
print(min(2, 5, 9, 4))
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print(math.modf(10.123))
# pow(x, y)	x**y 运算后的值。
print(pow(2, 5))
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print(round(3.4))
print(round(3.5))
# sqrt(x)	返回数字x的平方根
print(math.sqrt(4))
print(math.sqrt(9))
