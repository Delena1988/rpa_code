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
#
等额本金(865000, 3.1, 144 - 45)
