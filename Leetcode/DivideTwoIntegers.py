"""
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    这题解法太逗了，直接相减直到被减数<减数，减的次数就是商
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 保存符号
        flag = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        a = abs(dividend)
        b = abs(divisor)
        # 简单情况
        if a < b:
            return 0
        elif a == b:
            return flag

        if b==1:
            c = a*flag
        else:
            c = len(range(a, b-1, -b))*flag

        if -2**31 <= c <= 2**31-1:
            return c
        else:
            return 2**31-1


# print(Solution().divide(2147483647, 1))
# print(Solution().divide(-2147483648, 1))
# print(Solution().divide(-2147483648, -1))
print(Solution().divide(-2147483648, 2))
