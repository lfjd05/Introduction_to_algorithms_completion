"""
    给定一个 haystack 字符串和一个 needle 字符串，
    在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        if haystack=='' or len(haystack)<len(needle):
            return -1
        return haystack.find(needle)   # 这样太容易了，换一种

        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:len(needle)+i] == needle:
        #         return i
        # return -1


# print(Solution().strStr('hello', 'll'))
print(Solution().strStr('', ''))
