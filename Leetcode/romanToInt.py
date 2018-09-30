"""
    罗马数字转整数
"""
"""
    思路：罗马字从大到小排列遍历，复合就转化
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        output_list = []
        for i in range(len(s)):
            while value_list[i] <= num:   # 当罗马数小于这个数的时候循环
                output_list.append(roman_list[i])
                num -= value_list[i]
        return ''.join(i for i in output_list)


print(Solution().romanToInt("LVIII"))
