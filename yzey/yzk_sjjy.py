执行结果 = {"成功": {}, "失败": {}}
数据校验结果 = True

术后随访缺失记录 = ['56031', '谢广旭', '2023-12-21', '3', '2', '1', '查看详情', 90]

上一次随访数据字典 = {'随访时间': '2024-01-19', '体重': '50.4', '尿量_下拉': '正常', '尿量_数值': '1500.0',
                      '舒张压': '69', '收缩压': '123', '疲劳乏力': '无', '受体状态': '存活', '移植物状态': '带功',
                      '抗增殖类_药品': '赛可平',
                      '抗增殖类_剂量': '1000', '环孢素_药品': '', '环孢素_剂量': '', '他克莫司_药品': '赛氏他克莫司',
                      '他克莫司_剂量': '4.0', 'mTOR抑制剂_药品': '', 'mTOR抑制剂_剂量': '',
                      '激素_药品': '泼尼松(强的松)',
                      '激素_剂量': '10.0', '随访期间调整免疫抑制剂': '无', '血红蛋白': '127.0', '白细胞': '7.7',
                      '红细胞': '4.21', '血小板': '205.0', '淋巴细胞': '20.3', '中性粒细胞': '67.0', '尿蛋白定性': '—',
                      '血肌酐': '128.0', '尿素氮': '14.15', '血尿酸': '365.8', '谷丙转氨酶': '18.0',
                      '谷草转氨酶': '0.72',
                      '总胆红素': '9.7', '直接胆红素': '2.4', '白蛋白': '44.0', '球蛋白': '20.9', '总蛋白': '64.9',
                      '总胆固醇': '5.65', '甘油三酯': '1.22', '钠': '149.2', '钾': '4.01', '钙': '2.35',
                      '空腹血糖': '5.3'}

随访缺失数据字典 = {'他克莫司_药品': '普乐可复', '他克莫司_剂量': 2.0, '抗增殖类_药品': '赛可平', '抗增殖类_剂量': 1.0,
                    '激素_药品': '泼尼松（强的松）', '激素_剂量': 10.0, '尿蛋白定性': '阴性', '白细胞': '8.4',
                    '中性粒细胞': '77.0', '淋巴细胞': '14.1', '红细胞': '4.86', '血红蛋白': '141', '血小板': '184',
                    '总胆红素': '12.2', '直接胆红素': '3.00', '总蛋白': '69.2', '白蛋白': '47.1', '球蛋白': '22.1',
                    '谷草转氨酶': '14', '谷丙转氨酶': '19', '血肌酐': '110', '尿素氮': '4.79', '血尿酸': '163.5',
                    '空腹血糖': '4.79', '总胆固醇': '5.75', '甘油三酯': '1.74', '钾': '5.06', '钠': '141.3',
                    '钙': '2.73'}

新增缺失随访数据字典 = {}

取的上一次随访数据项 = []


def 数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, 数据项):
    if 数据项 not in 随访缺失数据字典:
        新增缺失随访数据字典[数据项] = 上一次随访数据字典[数据项]
        取的上一次随访数据项.append(数据项)
    else:
        新增缺失随访数据字典[数据项] = 随访缺失数据字典[数据项]


def 免疫抑制治疗数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, 数据项):
    药品 = 数据项 + '_药品'
    剂量 = 数据项 + '_剂量'
    if 药品 not in 随访缺失数据字典:
        if 上一次随访数据字典[药品] == '':
            新增缺失随访数据字典[药品] = ''
            新增缺失随访数据字典[剂量] = ''
        else:
            新增缺失随访数据字典['随访期间调整免疫抑制剂'] = '有'
    else:
        if 上一次随访数据字典[药品] == '' or 上一次随访数据字典[药品] != 随访缺失数据字典[药品]:
            新增缺失随访数据字典['随访期间调整免疫抑制剂'] = '有'
        新增缺失随访数据字典[药品] = 随访缺失数据字典[药品]
        新增缺失随访数据字典[剂量] = 随访缺失数据字典[剂量]

# 常规检查
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '体重')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '尿量_数值')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '舒张压')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '收缩压')

# 免疫抑制治疗
# 环孢素 和 他克莫司 不可连用
if '环孢素_药品' in 随访缺失数据字典 and '他克莫司_药品' in 随访缺失数据字典:
    数据校验结果 = False
if '抗增殖类_药品' not in 随访缺失数据字典 and '环孢素_药品' not in 随访缺失数据字典 and '他克莫司_药品' \
        not in 随访缺失数据字典 and 'mTOR抑制剂_药品' not in 随访缺失数据字典 and '激素_药品' not in 随访缺失数据字典:
    取的上一次随访数据项.append('免疫抑制治疗')

免疫抑制治疗数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '抗增殖类')
免疫抑制治疗数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '环孢素')
免疫抑制治疗数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '他克莫司')
免疫抑制治疗数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, 'mTOR抑制剂')
免疫抑制治疗数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '激素')
if '随访期间调整免疫抑制剂' not in 新增缺失随访数据字典:
    新增缺失随访数据字典['随访期间调整免疫抑制剂'] = '无'

# 实验室检查
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '血红蛋白')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '白细胞')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '红细胞')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '血小板')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '淋巴细胞')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '中性粒细胞')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '尿蛋白定性')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '血肌酐')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '尿素氮')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '血尿酸')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '谷丙转氨酶')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '谷草转氨酶')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '总胆红素')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '直接胆红素')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '白蛋白')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '球蛋白')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '总蛋白')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '总胆固醇')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '甘油三酯')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '钠')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '钾')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '钙')
数据校验(上一次随访数据字典, 随访缺失数据字典, 新增缺失随访数据字典, 取的上一次随访数据项, '空腹血糖')

print('数据校验结果: ' + str(数据校验结果))
print('取的上一次随访数据项: ' + str(取的上一次随访数据项))
print('新增缺失随访数据字典: ' + str(新增缺失随访数据字典))
