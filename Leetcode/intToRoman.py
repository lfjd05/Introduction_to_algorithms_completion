# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

"""
    思路：一个整数的组成问题，直接从大到小列出备选数，从大到小遍历，若罗马数字不大于num，
    则选用这个数，再用Num减去所选的数
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        output_list = []
        for i in range(len(value_list)):
            while value_list[i] <= num:   # 当罗马数小于这个数的时候循环
                output_list.append(roman_list[i])
                num -= value_list[i]
        return ''.join(i for i in output_list)

# print(Solution().intToRoman(58))

