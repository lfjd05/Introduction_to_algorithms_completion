# logn的解法，使用二分思想


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 找到两个升序数组的index, 夹逼方法
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pol = l
        # 搜索左半边
        ans = self.b_search(target, nums[:pol])
        if ans == -1:
            ans = self.b_search(target, nums[pol:])
            if ans != -1:
                ans += len(nums[:pol])  # 索引等于新索引加原来总长度
        return ans

    def b_search(self, target, nums):
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
        return index
