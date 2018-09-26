"""
    判断是否回文
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = list(str(x))
        if x_str == x_str[::-1]:
            return True
        else:
            return False


# print(Solution().isPalindrome(-121))