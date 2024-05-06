import pandas as pd

file_path = '/Users/linjian/PycharmProjects/rpa_code/gmrmyy/三个病区的出院表.xlsx'

raw_data = pd.read_excel(file_path, sheet_name='Sheet1', header=None)
# print(raw_data)
data = raw_data.values  # 只提取表中信息
df = pd.DataFrame(data)
# df_filtered  = df[(df[4] ==患者姓名)]

三个病区的出院患者列表 = [['2024-04-28 09:04:00', '田荣云', '13793630685', '心内二科病房', 'xn2', '1', '', '']]

for ele in 三个病区的出院患者列表:
    try:
        temp_bf= df[(df[1]==ele[7])][8].values[0]
        #if temp_bf!=ele[3]:
        if temp_bf=='EICU病房':
            ele[4] = 'eicu'
        elif temp_bf=='心内二科病房':
            ele[4] = 'xn2'
        elif temp_bf=='急诊科病房':
            ele[4] = 'jz'
    except IndexError:
        print('IndexError')

print(三个病区的出院患者列表)