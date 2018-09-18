"""
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 行数比较少的版本
        if len(s) != 0:
            r = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)
                 if s[i:i + x + 1] == s[i:i + x + 1][::-1]]
            # print(r)
            return r[-1]
        else:
            return s
        # for x in range(len(s)):
        #     for i in range(len(s)-x):
        #         a = s[i:i + x + 1]
        #         print(a, a[::-1])

# Solution().longestPalindrome('babad')
# Solution().longestPalindrome('cbbd')
