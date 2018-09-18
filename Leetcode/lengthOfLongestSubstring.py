# 给定一个字符串，找出不含有重复字符的最长子串的长度。
"""
遍历字符串中的每一个元素。借助一个辅助键值对来存储某个元素最后一次出现的下标。
用一个整形变量存储当前无重复字符的子串开始的下标。该元素下表减去开始下标就是不含重复字符串元素下标

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # write your code here
        res = 0
        if len(s) == 0:
            return res
        d = {}   # 某个元素最后出现的下标

# a   b   c   a   b   c   b   b
# start       i
        start = 0   # 无重复字符开始下标
        for i in range(len(s)):     # 遍历所有元素
            if s[i] in d and d[s[i]] >= start:      # 如果元素在d的key中，并且该元素是第二次出现
                start = d[s[i]] + 1                 # 这个元素的最后出现下标更新
            tmp = i - start + 1    # 计算无重复字符串长度
            d[s[i]] = i
            res = max(res, tmp)
        # print(res)
        return res

# Solution().lengthOfLongestSubstring('abcabcbb')
print('a'<'b'<'c')
