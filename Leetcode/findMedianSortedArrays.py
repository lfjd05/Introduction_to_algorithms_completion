"""
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)    # 排序很关键
        middle = len(nums)//2
        # print(nums)
        if len(nums)%2 == 0:            # 如果是奇数个
            # print((nums[middle-1]+nums[middle])/2)
            return (nums[middle-1]+nums[middle])/2
        else:
            # print(nums[middle])
            return nums[middle]

# Solution().findMedianSortedArrays([1, 3], [2])
# Solution().findMedianSortedArrays([1, 3], [3, 4])
