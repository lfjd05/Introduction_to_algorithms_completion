class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if '' in strs:   # 如果含有空串，最长公共前缀就是''
            return ''
        res = ''
        for each in zip(*strs):  # zip()函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
            if len(set(each)) == 1:  # 利用集合创建一个无序不重复元素集
                res += each[0]
            else:
                return res
        return res


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
