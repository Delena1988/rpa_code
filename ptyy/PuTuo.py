import pandas as pd


data = pd.read_excel('./糖尿病上报-2023-08-15.xls', header=0, index_col=0)
print(data.columns)
print(data.columns.get_loc('病人姓名'))
print(data.columns.get_loc('住院号'))
'''
# 获取excel行列数
# 获取行数
row_count = len(data)
# 获取列数
column_count = len(data.columns)
print(row_count)
print(column_count)
'''

'''
# Excel增加列
col_name = data.columns.tolist()  # 将列名全部提取出来存放在列表里
col_name.append('是否需上报')  # 将新增的列添加到最后
col_name.append('无需上报原因')  # 将新增的列添加到最后
col_name.append('上报结果')  # 将新增的列添加到最后
# DataFrame.reindex() 对原行/列索引重新构建索引值
data = data.reindex(columns=col_name)

是否需上报_数据 = ['是']
无需上报原因_数据 = ['']
上报结果_数据 = ['成功']

是否需上报_数据.append('否')
无需上报原因_数据.append('已上报过')
上报结果_数据.append('')

data['是否需上报'] = 是否需上报_数据  # 把新列的数据放到指定的列名下
data['无需上报原因'] = 无需上报原因_数据  # 把新列的数据放到指定的列名下
data['上报结果'] = 上报结果_数据  # 把新列的数据放到指定的列名下

data.to_excel('./糖尿病-2023-08-15.xlsx')  # 将整个data写入excel
'''

'''
# 用iloc方法修改数据
data = pd.read_excel('./糖尿病-2023-08-15.xlsx', header=0)
print(data.iloc[0, 0])
print(data.iloc[0, 1])
print(data.iloc[0, 2])
data.iloc[0, 5] = '是'
data.to_excel('./糖尿病-2023-08-15.xlsx')
'''


# for index, row in data.iterrows():
#     print(row['出院诊断'])
