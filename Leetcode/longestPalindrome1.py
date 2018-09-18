# 动态规划版本
"""
    v我们可以先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，
    这些必定是回文。然后计算所有长度为2的子字符串，再根据起始位置从左向右。
    到长度为3的时候，我们就可以利用上次的计算结果：如果中心对称的短字符串不是回文，
    那长字符串也不是，如果短字符串是回文，那就要看长字符串两头是否一样。
    这样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。
"""
"""
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
    https://segmentfault.com/a/1190000003914228
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2 or s == s[::-1]:
            return s
        n = len(s)
        start, maxlen = 0, 1   # 可以扩展的最大长度最小是1

        # i为回文串的右侧边界
        for i in range(1, n):

            odd = s[i - maxlen - 1:i + 1]  # 取得奇数串
            even = s[i - maxlen:i + 1]   # 取得偶数串

            if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlen - 1   # 这个回文串的起点位置
                maxlen += 2
                continue
            if i - maxlen >= 0 and even == even[::-1]:
                start = i - maxlen
                maxlen += 1

        # print(s[start:start + maxlen])
        return s[start:start + maxlen]


Solution().longestPalindrome('babad')
# Solution().longestPalindrome('cbbd')
