# leetcode试题，求两数之和
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        # 创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 字典d中存在nums[x]时
            if nums[x] in d:
                print(d[nums[x]], x)
                return d[nums[x]], x
            # 否则往字典增加键/值对
            else:
                d[a] = x
        # 边往字典增加键/值对，边与nums[x]进行对比


Solution().twoSum([3, 3], 6)
