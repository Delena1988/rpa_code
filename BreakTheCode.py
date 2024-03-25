import time
from typing import List
from tqdm import tqdm
from itertools import chain
from zipfile import ZipFile
import py7zr

start_time = time.time()

# chr(97) -> 'a' 这个变量保存了密码包含的字符集
'''
dictionaries = [chr(i) for i in
                 chain(range(97, 123),    # a - z
                       range(65, 91),    # A - Z
                       range(48, 58))]    # 0 - 9
'''

# 设置数字密码库0-9
dictionaries = [str(i) for i in range(10)]
print(dictionaries)


# 1. 生成可能的密码库
def all_passwd(dictionaries: List[str], maxlen: int):
    # 返回由 dictionaries 中字符组成的所有长度为 maxlen 的字符串
    def helper(temp: list, start: int, n: int):
        # 辅助函数，是个生成器
        if start == n:  # 达到递归出口
            yield ''.join(temp)
            return
        for t in dictionaries:
            temp[start] = t  # 在每个位置
            yield from helper(temp, start + 1, n)

    yield from helper([0] * maxlen, 0, maxlen)


# 2. 破解密码
def cracking_passwords(file_path: str, pwd: str, save_path: str) -> bool:
    # if py7zr.is_7zfile(file_path):
    #     print("This is a true 7z file!")
    try:
        with py7zr.SevenZipFile(file_path, mode='r', password=pwd) as z:
            # 解压到当前目录
            z.extractall(path='.')

        # 密码输入错误的时候会报错
        now_time = time.time()  # 故使用 try - except 语句
        # 将正确的密码输出到控制台
        print(f'恭喜破解成功：压缩文件的密码是: {pwd}')
        print(f'破解时长：{now_time - start_time}秒')
        return True
    except:
        return False


if __name__ == '__main__':
    # 设置密码长度
    lengths = [4]
    # 获取密码的组合数
    total = sum(len(dictionaries) ** n for n in lengths)
    for password in tqdm(chain.from_iterable(all_passwd(dictionaries, maxlen) for maxlen in lengths), total=total):
        # 如果破解成功，程序结束，./ 表示解压到当前目录
        if cracking_passwords('/Users/linjian/Downloads/yjm.7z', password, '/Users/linjian/Downloads'):
            break
