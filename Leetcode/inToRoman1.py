# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

"""
    解法2
    思路：每个罗马字都是各个位数加起来的。例如58=50+8=L+(VIII),将各个位数求余数拿出来以后分别组合
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 个位 0,1-9
        bit1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        # 十位 空，10-90
        bit2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        # 百位 空，100-900
        bit3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # 千位 空，1000-3000
        bit4 = ["", "M", "MM", "MMM"]

        # 例如取出20的十位，就是20%100=20 再 //10=2
        output_list = bit4[num // 1000] + bit3[(num % 1000) // 100] + bit2[(num % 100) // 10] + bit1[num % 10]

        return output_list


# print(Solution().intToRoman(58))