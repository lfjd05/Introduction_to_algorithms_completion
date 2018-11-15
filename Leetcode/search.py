class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1

        # 如果在最大最小的以外直接返回
        if target < min(nums) or target > max(nums):
            return -1
        try:
            location = nums.index(target)

            return location
        except ValueError:
            return -1


print(Solution().search([4,5,6,7,0,1,2], target=3))
