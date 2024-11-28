import datetime


def compareTime():
    # return True
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dateStr1 = datetime.datetime.now().strftime("%Y-%m-%d") + ' 00:00:00'
    dateStr2 = datetime.datetime.now().strftime("%Y-%m-%d") + ' 03:58:59'
    dateStr3 = datetime.datetime.now().strftime("%Y-%m-%d") + ' 10:00:00'
    dateStr4 = datetime.datetime.now().strftime("%Y-%m-%d") + ' 13:58:59'


from datetime import datetime


# 根据出生日期计算年龄
def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    current_date = datetime.now()
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def replacLastChar(text, char):
    index = text.rfind(char)
    if index == -1:
        return text
    else:
        return text[:index] + text[index + 1:]




# address = '浙江省宁波市鄞州区钟公庙街道钟公庙社区居门委牌会号'
address = '浙江省宁波市鄞州区钟公庙街道钟公庙社区居委会'
address = replacLastChar(address, '号')
address = replacLastChar(address, '牌')
address = replacLastChar(address, '门')
print(address)
# print(calculate_age("2017-12-30"))
