import pandas as pd

data = pd.read_excel('/Users/linjian/PycharmProjects/rpa_code/excel/excel文件.xlsx', header=0)
print(data)
print(data.loc[1, '姓名'])
print(data.iloc[1, 3])
