import pandas as pd

df = pd.read_excel('/Users/linjian/PycharmProjects/rpa_code/yzey/血透室检验RPA.xlsx', sheet_name='Sheet1', header=0,
                   dtype=object)
row_count = df.shape[0]  # 返回df的行数
col_count = df.shape[1]  # 返回df的列数

检验套餐字典 = dict()
特殊患者字典 = dict()

for row in df.itertuples():
    月份 = row[1]
    if 月份 in 检验套餐字典:
        检验项目集合 = set(检验套餐字典[月份])
    else:
        检验项目集合 = set()

    for i in range(2, len(df.columns) + 1):
        if row[i] == row[i]:
            检验项目集合.add(row[i])
    检验套餐字典[月份] = list(检验项目集合)

print(检验套餐字典)

df2 = pd.read_excel('/Users/linjian/PycharmProjects/rpa_code/yzey/血透室检验RPA.xlsx', sheet_name='Sheet2', header=0,
                    dtype=object)
row_count = df.shape[0]  # 返回df的行数
col_count = df.shape[1]  # 返回df的列数

for row in df2.itertuples():
    姓名 = row[1]
    月份 = row[2]
    类型 = row[3]
    检验项目 = row[4]
    姓名_月份_类型 = 姓名 + '_' + 月份 + '_' + 类型
    if 姓名_月份_类型 in 特殊患者字典:
        temp = 特殊患者字典[姓名_月份_类型]
        temp.add(检验项目)
        特殊患者字典[姓名_月份_类型] = temp
    else:
        temp = set()
        temp.add(检验项目)
        特殊患者字典[姓名_月份_类型] = temp

print(特殊患者字典)

姓名 = '张三'
月份 = '5月份'
患者检验项目 = set(检验套餐字典[月份])
if 姓名 + '_' + 月份 + '_增加' in 特殊患者字典:
    增加项目 = set(特殊患者字典[姓名 + '_' + 月份 + '_增加'])
    患者检验项目 = 患者检验项目 | 增加项目
if 姓名 + '_' + 月份 + '_删减' in 特殊患者字典:
    删减项目 = set(特殊患者字典[姓名 + '_' + 月份 + '_删减'])
    患者检验项目 = 患者检验项目 - 删减项目

患者检验项目 = list(患者检验项目)
print(患者检验项目)
