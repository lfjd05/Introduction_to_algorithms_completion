"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

分析：
若 p=None s=None return True
   p!=None s=None return False
   p = None s!=None return False 无法匹配
   长度 p=1 s=1 只有 p==s或者p='.' 的时候为true
   长度 !=1时候
   如果第二个字符不是*判断第一个字符是否相等，从第二个字符开始递归
   如果第二个字符是*且匹配，调用递归匹配s和去掉前两个字符的p
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

