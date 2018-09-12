# 牛客网题目：1016.部分A+B
"""
    正整数A的“DA（为1位整数）部分”定义为由A中所有DA组成的新整数PA。例如：给定A = 3862767，DA = 6，则A的“6部分”PA是66，因为A中有2个6。

    现给定A、DA、B、DB，请编写程序计算PA + PB。
"""
import re


def mut_input():
    a, da, b, db = [each for each in input().split()]
    return a, da, b, db


def find_papb(a, da, b, db):
    # 匹配字符
    pa = re.findall('[{}]+'.format(da), a)
    pb = re.findall('[{}]+'.format(db), b)

    if len(pa) < 1:
        pa_str = 0
    else:
        pa_str = int(''.join(pa))
    if len(pb) < 1:
        pb_str = 0
    else:
        pb_str = int(''.join(pb))
    print(pa_str+pb_str)

A, Da, B, Db = mut_input()
# A, Da, B, Db = '3862767', '6', '13530293', '3'
find_papb(A, Da, B, Db)
