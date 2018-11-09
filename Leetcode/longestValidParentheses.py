# 栈的解法


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 简单情况
        if len(s) == 0:
            return 0
        stack = []
        max_len = 0
        st = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # ')'但栈里面没有'('配对
                if len(stack) == 0:
                    st = i+1
                    continue
                else:
                    stack.pop()
                    if len(stack) == 0:
                        # 完成一次配对更新maxlen
                        max_len = max(i-st+1, max_len)
                    else:
                        # 还有计算和栈顶索引相减
                        max_len = max(i-stack[-1], max_len)
        return max_len


# print(Solution().longestValidParentheses("(()"))
# print(Solution().longestValidParentheses(")()())"))
print(Solution().longestValidParentheses("()(()"))