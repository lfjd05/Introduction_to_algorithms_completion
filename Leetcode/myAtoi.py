# coding=utf-8
"""
    实现 atoi，将字符串转为整数。

该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。
"""
import re


class Solution(object):
    def myAtoi(self, str0):
        """
        :type str: str
        :rtype: int
        """
        # 第一个字符是字母返回0
        try:
            if str(list(str0)[0]).isalpha():
                return 0
            elif str(list(str0)[0]).startswith('+') and str(list(str0)[1]).startswith('-'):
                return 0
            elif str(list(str0)[0]).startswith('+') and (not str(list(str0)[1]).startswith('-')):
                str0 = str0.replace('+', '')
        except IndexError:
            return 0
        try:
            result = int(float(re.sub("[A-Za-z]+", "", str0.strip())))
        except ValueError:
            return 0
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        elif result < -2 ** 31:
            return -2 ** 31
        else:
            return 2 ** 31 - 1


# print int(3.14159)
# a = " 42"
# a = "4193 with words"
# a = "words and 987"
# a = "3.14159"
# a = '+100'
a = "+-2"
print Solution().myAtoi(a)
