# 可以用在多位数组合上面


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # 添加首元素
        res = [i for i in digit2chars[digits[0]]]

        # 后几个元素循环
        for i in digits[1:]:
            res = [m + n for m in res for n in digit2chars[i]]
            # print(res)

        return res


print(Solution().letterCombinations('2345'))
