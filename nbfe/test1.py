import re


n,y,r,s,f = '','','','',''

patternG = re.escape('于') + r'(\d*?)' + re.escape('年')
patternP = re.escape('年') + r'(\d*?)' + re.escape('月')
patternY = re.escape('月') + r'(\d*?)' + re.escape('日 ')
patternX = re.escape('日 ') + r'(\d*?)' + re.escape('时')
patternF = re.escape('时') + r'(\d*?)' + re.escape('分')

message = '6、娩出胎儿方法：取胎头困难，于单叶产钳助产，于2024年03月06日 14时31分娩出胎头，头位，。'

matchG = re.search(patternG, message)
matchP = re.search(patternP, message)
matchY = re.search(patternY, message)
matchX = re.search(patternX, message)
matchF = re.search(patternF, message)

if matchG:
    n = matchG.group(1)
if matchP:
    y = matchP.group(1)
if matchY:
    r = matchY.group(1)
if matchX:
    s = matchX.group(1)
if matchF:
    f = matchF.group(1)


# print(matchG.group(0))
# print(matchP.group(1))
print(n, y, r,s,f)