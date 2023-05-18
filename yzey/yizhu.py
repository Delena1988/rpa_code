import pandas as pd

df = pd.read_excel('/Users/linjian/PycharmProjects/rpa_code/yzey/血透开立医嘱RPA.xlsx', header=0,dtype=object)
row_count = df.shape[0]  # 返回df的行数
col_count = df.shape[1]  # 返回df的列数
# print(row_count)
# print(col_count)

医嘱总字典 = dict()
血透患者 = set()

for i in range(0, row_count):
    # print(df.loc[i,'医嘱名称'])
    姓名 = df.loc[i, '姓名']
    身份证 = df.loc[i, '身份证']
    就诊卡号 = str(df.loc[i, '就诊卡号'])
    诊断 = df.loc[i, '诊断']
    医嘱类型 = df.loc[i, '医嘱类型']
    医嘱名称 = df.loc[i, '医嘱名称']
    每次量 = df.loc[i, '每次量']
    单位 = df.loc[i, '单位']
    用法 = df.loc[i, '用法']
    频次 = df.loc[i, '频次']
    天数 = df.loc[i, '天数']
    总量 = df.loc[i, '总量']
    院注次数 = df.loc[i, '院注次数']

    # 参数校验
    # if str(姓名) == 'nan':
    #     logging.info('第 ' + str(i) + ' 行姓名为空')
    #     continue
    if pd.isna(姓名):
        姓名 = None
    if pd.isna(身份证):
        身份证 = None
    if pd.isna(每次量):
        每次量 = None
    if pd.isna(单位):
        单位 = None
    if pd.isna(用法):
        用法 = None
    if pd.isna(频次):
        频次 = None
    if pd.isna(天数):
        天数 = None
    if pd.isna(总量):
        总量 = None
    if pd.isna(院注次数):
        院注次数 = None
    医嘱字典 = {'医嘱名称': 医嘱名称, '每次量': 每次量, '单位': 单位, '用法': 用法, '频次': 频次, '天数': 天数,
                '总量': 总量, '院注次数': 院注次数}
    # 血透患者集合
    血透患者.add(姓名)

    # 医嘱处理
    姓名_就诊卡号 = str(姓名) + '_' + str(就诊卡号)

    if 姓名_就诊卡号 in 医嘱总字典:
        if 医嘱类型 == '特病':
            if '特病医嘱' in 医嘱总字典[姓名_就诊卡号]:
                医嘱总字典[姓名_就诊卡号]['特病医嘱'][医嘱名称] = 医嘱字典
            else:
                temp = {医嘱名称: 医嘱字典}
                医嘱总字典[姓名_就诊卡号]['特病医嘱'] = temp
        else:
            if '普通医嘱' in 医嘱总字典[姓名_就诊卡号]:
                医嘱总字典[姓名_就诊卡号]['普通医嘱'][医嘱名称] = 医嘱字典
            else:
                temp = {医嘱名称: 医嘱字典}
                医嘱总字典[姓名_就诊卡号]['普通医嘱'] = temp
    else:
        temp = {医嘱名称: 医嘱字典}
        if 医嘱类型 == '特病':
            temp1 = {'特病医嘱': temp}
        else:
            temp1 = {'普通医嘱': temp}
        医嘱总字典[姓名_就诊卡号] = temp1

print(医嘱总字典)
print(血透患者)

