"""
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        d = {'(':')', '[':']', '{': '}'}
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    a = stack.pop()
                    if d[a]==i:
                        continue
                    else:
                        return False
        if len(stack) != 0:
            return False
        return True


# "{[]}"
print(Solution().isValid("{[]}"))
