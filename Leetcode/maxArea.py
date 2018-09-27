"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。

n>=2
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        可以看出来面积是短的那端决定的
        逼近法
                每次左右两端都舍去短的那一端
        若选择短的那一端【S=小于等于此端的高*小于等于当前的最大区间长度】
        至多的面积也是选择最左最右的一个矩形，因此不必再考虑短的一端，直接舍去逼近
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while right > left:
            # 水的面积是短的那端决定的
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            # 舍去短的
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
