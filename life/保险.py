本金 = 20000
利率 = 0.02
年数 = 10

total = 0
for i in range(0, 10):
    total = total + 本金 * (1 + 0.02) ** i

print(total)
