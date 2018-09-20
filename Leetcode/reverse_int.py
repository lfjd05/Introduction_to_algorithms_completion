# coding=utf-8
"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
示例 2:

输入: -123
输出: -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x.startswith('-'):
            x = list(x.strip('-'))[::-1]
            # print int('-'+''.join(str(i) for i in x))
            result = int('-'+''.join(str(i) for i in x))
        else:
            x = list(x)[::-1]
            # print int(''.join(str(i) for i in x))
            result = int(''.join(str(i) for i in x))
        if -2**31<=result<=2**31-1:
            return result
        else:
            return 0


# a = 123
# a = -123
# a = -120
# a = 1534236469
# print Solution().reverse(a)
