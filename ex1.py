"""
    给定备选组数字，组成多位数
"""


class Solution:
    def letterCombinations(self, digits, bit):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        num_list = list(digits)

        # 添加首元素
        # res = [0 for i in range(bit)]
        res = num_list

        # 后几个元素循环
        for i in range(bit-1):
            res = [m + n for m in res for n in num_list]
            # print(res)

        return res


print(Solution().letterCombinations('2345', 2))
