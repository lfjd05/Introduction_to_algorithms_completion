"""
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]