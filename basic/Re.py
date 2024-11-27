import re

# 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())
# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))
print(re.search('com', 'www.runoob.com').span())
print()

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.groups() : ", matchObj.groups())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

print("=============检索和替换=============")
phone = "2004-959-559 # 这是一个国外电话号码"

print("原号码：", phone)
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
print()

print("=============group=============")
text = "abc123def456"
# 每个分组都可以通过小括号括起来，用于将匹配结果分成多个组，可以通过在group方法中指定分组编号来获取指定分组的匹配结果。
pattern = re.compile(r'(\d+)(\w+)')
match = re.search(pattern, text)
print("text: ", text, "\t", "pattern: ", pattern)
print("groups: ", match.groups())
print("group0: ", match.group(0))
print("group1: ", match.group(1))
print("group2: ", match.group(2))
print()

print("=============start、end、span=============")
# 从'1'的位置开始匹配，正好匹配
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four', 3, 10)
print('start: ', m.start(0))
print('end: ', m.end(0))
print('span: ', m.span(0))
print()

print("=============findall=============")
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
print()

print("=============finditer=============")
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
print()

print("=============split=============")
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
