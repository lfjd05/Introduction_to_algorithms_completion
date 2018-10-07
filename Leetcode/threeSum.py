"""
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
    使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
"""


class Solution:
    def threeSum(self, nums):
        """
        数组排序，遍历数组，用夹逼方法找到另外两个解
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        # 可以添加正负划分

        result = []
        for i in range(len(nums)):
            # 相邻的数相等不需要再计算几次，因为结果肯定一样
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1   # 从i到最后一个元素开始夹逼
            right = len(nums)-1
            while left < right:
                sum0 = nums[i] + nums[left]+nums[right]
                if 0 == sum0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 相邻元素相等就不再用
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif 0 > sum0:  # 太小了，左侧逼近
                    left += 1
                else:
                    right -= 1
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
