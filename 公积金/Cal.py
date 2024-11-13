from datetime import datetime


def months_between(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')

    years = date2.year - date1.year
    months = date2.month - date1.month
    # 如果月份差小于0，则年份需要减去1
    if months < 0:
        years -= 1
        months += 12
    return 12 * years + months

def 等额本金(贷款金额, 贷款利率, 还款月数):
    剩余贷款本金 = 贷款金额
    每月还款本金 = 贷款金额 / 还款月数
    for 月份 in range(1, 还款月数):
        每月还款利息 = 剩余贷款本金 * 贷款利率 / 100 / 10
        剩余贷款本金 = 剩余贷款本金 - 每月还款本金
        每月还款总额 = 每月还款本金 + 每月还款利息
        print(str(月份) + "::: " +
              "本金: " + str(round(每月还款本金, 2)) + " 利息: " + str(round(每月还款利息, 2)) +
              " 总额: " + str(round(每月还款总额, 2)) + " 剩余本金: " + str(round(剩余贷款本金, 2)))


# 三十年
# 等额本金(1000000, 3.575, 360)
# 十年
# 等额本金(1000000, 3.575, 120)
#
# 20240820 10588.92  8311.01 2277.91
# 20330318
date1 = '2024-09-18'
date2 = '2032-03-18'
print(months_between(date1, date2))

# 等额本金(756301.85, 3.575, 91)
等额本金(756301.85, 3.325, 91)