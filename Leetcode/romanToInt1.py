"""
    和inttoraman.py类似的思路，就是反过来，这个数据结构改用字典存储，击败26.88%
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
                      'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        # 列表推导式
        output_list = [roman_list[s[i]] if roman_list[s[i]] >= roman_list[s[i + 1]]
                       else -roman_list[s[i]]
                       for i in range(len(s) - 1)]
        print(output_list)
        return sum(output_list) + roman_list[s[-1]]

# print(Solution().romanToInt("III"))
# print(Solution().romanToInt("LVIII"))    # 54
# print(Solution().romanToInt("MCMXCIV"))   # 1995
