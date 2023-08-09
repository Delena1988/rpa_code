import pandas as pd

data = pd.read_excel('./医院论文数据样例.xlsx', header=0)
deptList = []
for index, row in data.iterrows():
    Addresses = row['Addresses'].replace('[', '').replace(']', '')
    # print(Addresses)
    list = Addresses.split(',')
    for tmp in list:
        tmp = tmp.lstrip()
        if (tmp.startswith('Dept') and tmp not in deptList):
            deptList.append(tmp)

print(deptList)

