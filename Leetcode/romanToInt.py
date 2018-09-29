"""
    和inttoraman.py类似的思路，就是反过来，这个数据结构不好，比较费时间，击败23.93%
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        # 列表推导式
        output_list = [-value_list[roman_list.index(s[i])] if roman_list.index(s[i])>roman_list.index(s[i+1])
                       else value_list[roman_list.index(s[i])]
                       for i in range(len(s) - 1)]
        return sum(output_list)+value_list[roman_list.index(s[-1])]


# print(Solution().romanToInt("III"))
# print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
