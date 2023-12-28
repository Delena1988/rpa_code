from datetime import datetime

# 根据出生日期计算年龄
# 出生日期格式 2021-03-25 or 2021-03-25 19:20:39
def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str.split(" ")[0], "%Y-%m-%d")
    current_date = datetime.now()
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


print(calculate_age("2021-03-25"))
print(calculate_age("2021-03-25 19:20:39"))