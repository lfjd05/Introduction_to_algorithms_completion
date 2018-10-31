class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        # 如果全都不一样
        if len(nums) == len(set(nums)):
            return len(nums)
        new_len = 1

        for index,item in enumerate(nums):
            if index == 0:
                continue
            if item != nums[index-1]:   # 如果不相等则更改数值
                nums[new_len] = item
                new_len += 1
        return new_len


print(Solution().removeDuplicates([1, 1, 2]))