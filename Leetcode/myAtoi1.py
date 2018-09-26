# coding=utf-8
"""
    非空字符是正号或负号，选取该符号，
    并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        maxint = 0x7fffffff
        minint = 0x80000000
        max = 0x80000000
        ans = 0
        flag = False
        st = 0

        # 第一个非空的字符必须是正负或者数字
        while st < len(str) and str[st] == ' ':   # 判断空格
            st += 1
        if st < len(str) and str[st] == '+':   # 如果第一位是正号
            st += 1
        else:
            if st < len(str) and str[st] == '-':
                flag = True
                st += 1
        for i in range(st, len(str)):
            try:
                if 9 >= int(str[i]) >= 0:   # 如果该索引位置是数字
                    ans = ans * 10 + int(str[i])

                    if ans > maxint:
                        ans = max
            except ValueError:    # 应该是数字的索引位置遇到负号
                break

        if flag:
            ans = -ans
            if ans < -minint:
                ans = -minint
        if ans > maxint:
            ans = maxint
        return ans


# print int(3.14159)
# a = " -42"
# a = "4193 with words"
a = "words and 987"
# a = "3.14159"
# a = '+100'
# a = "+-2"
print Solution().myAtoi(a)
