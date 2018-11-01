"""
    给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        # 如果都不在这里面，就别捣乱了
        if val not in nums:
            return len(nums)
        new_len = len(nums)

        index = 0
        while index < new_len:
            if val == nums[index]:
                nums.insert(len(nums), nums[index])   # 相等元素插入到最后
                nums.remove(nums[index])
                new_len -= 1   # 原数组长度-1
                continue
            index += 1
        # print(nums)
        return new_len


# print(Solution().removeElement([3,2,2,3], 3))
# print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))