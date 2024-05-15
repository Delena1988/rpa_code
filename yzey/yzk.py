import re

line = '缺失随访次数1次 缺失4320天随访'
line.split(" ")

pattern = r'.*缺失随访次数*\d+次'
pattern1 = r'.*缺失*\d+天随访'
match_obj = re.findall(pattern, line)
# if len(match_obj) >= 1:
#     print(match_obj)
#     print(int((re.findall(pattern, match_obj[0]))[0]))

缺失随访次数 = re.findall(r'\d+', line)
缺失随访天数 = re.findall(r'\d+', line)
print(缺失随访次数)
# match_obj = re.findall(pattern1, line)

# print(re.match('有.*糖尿病.*史[0-9]*年', line, ))
# res = re.search(r'糖尿病', line)
