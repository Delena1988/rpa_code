import pandas as pd

pd.set_option('display.max_rows', 500)  # 设置展示最高行数
pd.set_option('display.max_columns', 1000)  # 设置展示最高列数
pd.set_option('display.unicode.east_asian_width', True)  # 设置列名对齐
# 导入数据
df = pd.read_excel(r"/Users/linjian/Downloads/人工成本分摊V1-机器人对接0427.xlsx", sheet_name="导出-工资")
# 劳务求和
df1 = df[df['ccode'] == 52010101]
项目求和 = df1.groupby('citem_id', as_index=False)['md'].sum()
print(项目求和)
# 导出df
df_new = pd.DataFrame(
    columns=['iperiod', 'isignseq', 'inid', 'dbill_date', 'idoc', 'cbill', 'cdigest', 'ccode', 'md', 'mc', 'cdept_id',
             'cperson_id', 'ccus_id', 'csup_id', 'citem_id', 'citem_class'])
i = 1
for row in df.index:
    df.loc[row, 'inid'] = i
    if (df.loc[row]['ccode'] == 52010101):
        pro_code = df.loc[row, 'citem_id']
        if (not df_new[df_new['citem_id'] == pro_code].empty):
            continue
        else:
            df.loc[row, 'md'] = round(项目求和[项目求和['citem_id'] == pro_code].iloc[0, 1], 2)
    df_new.loc[len(df_new)] = df.loc[row]
    i = i + 1
    # print(df_new)
