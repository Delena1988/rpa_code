import pandas as pd

df = pd.read_excel('/Users/linjian/PycharmProjects/rpa_code/yzey/血透开立医嘱RPA.xlsx', header=0, dtype=object)
row_count = df.shape[0]  # 返回df的行数
col_count = df.shape[1]  # 返回df的列数

医嘱总字典 = dict()
透析患者 = set()

for i in range(0, row_count):
    姓名 = df.loc[i, '姓名']
    电话 = df.loc[i, '电话']
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
    if pd.isna(电话):
        电话 = None
    if pd.isna(就诊卡号):
        就诊卡号 = None
    if pd.isna(诊断):
        诊断 = None
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
    # 透析患者集合
    透析患者.add(姓名)

    # 医嘱处理
    姓名_就诊卡号 = str(姓名) + '_' + str(就诊卡号)

    if 姓名_就诊卡号 in 医嘱总字典:
        # 诊断
        if 诊断 is not None:
            if '诊断' in 医嘱总字典[姓名_就诊卡号]:
                temp = 医嘱总字典[姓名_就诊卡号]['诊断']
                temp.add(诊断)
                医嘱总字典[姓名_就诊卡号]['诊断'] = temp
            else:
                temp = set()
                temp.add(诊断)
                医嘱总字典[姓名_就诊卡号]['诊断'] = temp

        # 医嘱
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
        if 诊断 is not None:
            temp2 = set()
            temp2.add(诊断)
            temp1.update({'诊断': temp2})
        医嘱总字典[姓名_就诊卡号] = temp1


print(医嘱总字典)
print(透析患者)
