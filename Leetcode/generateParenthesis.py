"""
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generateParenthesisIter('', n, n)
        return self.res

    def generateParenthesisIter(self, mstr, r, l):
        """

        :param mstr:
        :param r:   右侧括号数量
        :param l:   左侧括号数量
        :return:
        """
        if r == 0 and l == 0:
            # 左右都不剩余说明排完了
            self.res.append(mstr)
        # 如果左括号还有剩余，则可以放置左括号，如果右括号的剩余数大于左括号，则可以放置右括号
        if l > 0:
            self.generateParenthesisIter(mstr+'(', r, l-1)
        if r > 0 and r > l:   # 假如剩余的右括号还比较多
            self.generateParenthesisIter(mstr+')', r-1, l)


# print(Solution().generateParenthesis(3))