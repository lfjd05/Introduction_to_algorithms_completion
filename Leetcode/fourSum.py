"""
    四个数之和，简单的把3数之和赋值过来多加一层循环
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        sum_list = []

        # 先考虑特殊情况
        if len(nums)==0 or len(nums)<4:
            return sum_list

        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return sum_list

        if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return sum_list
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-2):
                left = j + 1  # 从i到最后一个元素开始夹逼
                right = len(nums) - 1
                while left < right:
                    sum0 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum0 == target:
                        if sorted([nums[i], nums[j], nums[left], nums[right]]) not in sum_list:
                            sum_list.append(sorted([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1
                        # 如果一样就移动一下
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum0 > target:  # 太小了，左侧逼近
                        right -= 1
                        # 相邻元素相等再移动
                        while left < right - 1 and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        left += 1
                        while left < right - 1 and nums[left] == nums[left - 1]:
                            left += 1
        return sum_list


# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
# print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))
# print(Solution().fourSum([2,-4,-5,-2,-3,-5,0,4,-2],-14))

