import pandas as pd

data = pd.read_excel('./糖尿病上报-2023-08-15.xlsx', header=0, index_col=0)
row_count = len(data)
需上报数据字典 = dict()

for i in range(0, row_count):
    住院记录 = data.iloc[i]
    # 病人姓名 = data.iloc(i + 1)['病人姓名']
    print(住院记录)
