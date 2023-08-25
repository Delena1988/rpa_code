import pandas as pd


data = pd.read_excel('./糖尿病上报-2023-08-15.xlsx', header=0, index_col=0)

# Excel增加列
col_name = data.columns.tolist()  # 将列名全部提取出来存放在列表里
col_name.append('是否需上报')  # 将新增的列添加到最后
col_name.append('无需上报原因')  # 将新增的列添加到最后
col_name.append('上报结果')  # 将新增的列添加到最后
# DataFrame.reindex() 对原行/列索引重新构建索引值
data = data.reindex(columns=col_name)

是否需上报_数据 = []
无需上报原因_数据 = []
上报结果_数据 = []

for index, row in data.iterrows():
    是否需上报 = '否'
    # 1.恶性肿瘤维持性化学治疗；2.恶性肿瘤靶向治疗；3.乳腺恶性肿瘤(IV期)；4.肝继发恶性肿瘤；5.骨继发恶性肿瘤；6.高血压；7.2型糖尿病；
    出院诊断数组 = row['出院诊断'].split('；')
    for 出院诊断 in 出院诊断数组:
        if 出院诊断[2:] != '糖尿病的特殊筛查' and '糖尿病' in 出院诊断[2:]:
            是否需上报 = '是'
            break
    是否需上报_数据.append(是否需上报)
    if(是否需上报 == '否'):
        无需上报原因_数据.append('出院诊断不符合')
    else:
        无需上报原因_数据.append('')

data['是否需上报'] = 是否需上报_数据  # 把新列的数据放到指定的列名下
data['无需上报原因'] = 无需上报原因_数据  # 把新列的数据放到指定的列名下
# data['上报结果'] = 上报结果_数据  # 把新列的数据放到指定的列名下

# print(data)
data.to_excel('./糖尿病上报-2023-08-15.xlsx')  # 将整个data写入excel