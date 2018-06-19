"""
    基本的初等数学类
    最大公约数，公倍数，素因子分解，闰年判断，找零钱，斐波那契数列
    参考：https://github.com/yidao620c/core-algorithm/blob/master/ch01_basic/at001_math.py
"""


# 如果是整百年，能被400整除，是闰年，或者不能被100整除，能被4整除
# 是闰年返回true
def LeapYear(year):
    return print((year % 4 == 0 and (year % 100 != 0)) or (year % 400 == 0))


# 辗转相除求最大公约数
def maxcommondivisor(m, n):
    while True:
        remainder = m % n
        # 如果余数为零，则较小的为公约
        if not remainder:    # 如果remainder为0，返回true
            return n
        else:
            m, n = n, remainder  # 余数不为0，用较小数除刚才的余数


# 最小公倍数为两个数积除最打公约数
def maxcommonmultiple(m, n):
    return m * n / maxcommondivisor(m, n)


# 判断素数
def prime(n):
    result = True
    # 0-1 不包括1，步长为-1
    for i in range(int(n / 2), 1, -1):
        if n % i == 0:
            result = False
            break
    return print('素数', result)


# 因式分解
def factors(n):
    result = [n]
    for i in range(int(n/2), 0, -1):  # 只需要循环一半即可
        if n % i == 0:
            result.append(i)
    return print('因子', result)


# 斐波那契序列,前2为1，第三项为前两个之和
def fibonacci(n):
    result = []
    if n == 1:
        result.append(1)
    else:
        result.append(1)
        result.append(1)
        for i in range(2, int(n)):
            result.append((result[-1]+result[-2]))
    return print('前n个斐波那契数列是', result)

if __name__ == '__main__':
    LeapYear(1600)
    prime(73)
    factors(225)
    fibonacci(225)
