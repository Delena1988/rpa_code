TXT解析字典 = {}
TXT解析列表 = []
fileHandler = open('王维_24305312_1.txt', "r")
while True:
    line = fileHandler.readline()
    if not line:
        break
    TXT解析列表.append(line.strip())
fileHandler.close()

print(TXT解析列表)

for item in TXT解析列表:
    if ':   ' in item:
        item.replace(':   ', ':')
    elif ':   ' in item:
        item.replace(':   ', ':')
    elif ': ' in item:
        item.replace(': ', ':')

    if '：   ' in item:
        item.replace('：   ', ':')
    elif '： ' in item:
        item.replace('： ', ':')
    elif '： ' in item:
        item.replace('： ', ':')
    # item = item.replace(':   ', ':').replace(':   ', ':').replace(': ', ':')
    # item = item.replace('：   ', '：').replace('： ', '：').replace('： ', '：')
    print(item)
    item = item.replace("头围", "  头围")
    item = item.replace("性别", "  性别")
    print(item)
    split = item.split('  ')
    for i in split:
        if i != '' and len(i) > 0 and '：' in i:
            TXT解析字典[i.strip().split('：')[0]] = i.strip().split('：')[1] if len(i.strip().split('：')) > 1 else ''
        elif i != '' and len(i) > 0 and ':' in i:
            TXT解析字典[i.strip().split(':')[0]] = i.strip().split(':')[1] if len(i.strip().split(':')) > 1 else ''
print(TXT解析字典)
