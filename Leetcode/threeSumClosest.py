"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        sum_list = 0
        min_value = 99999
        for i in range(len(nums)):
            left = i + 1   # 从i到最后一个元素开始夹逼
            right = len(nums)-1
            while left < right:
                sum0 = nums[i] + nums[left]+nums[right]
                diff = abs(target-sum0)
                if diff < min_value:
                    sum_list=sum0
                    min_value = diff
                if sum0>target:  # 太小了，左侧逼近
                    right -= 1
                    # 相邻元素相等就不再用
                    while left < right-1 and nums[right] == nums[right-1]:
                        right -= 1
                else:
                    left += 1
                    while left < right-1 and nums[left] == nums[left+1]:
                        left += 1
        return sum_list


# print(Solution().threeSumClosest([-1, 2, 1, -4], 1))  # 2
# print(Solution().threeSumClosest([0, 0, 0], 1))    # 0
# print(Solution().threeSumClosest([1, 1, 1, 0], -100))  # 2
print(Solution().threeSumClosest([0, 2, 1, -3], 1))  # 0
