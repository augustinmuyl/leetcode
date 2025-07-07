class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            print(m)
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        m = (l + r) // 2
        if m < 0:
            m = 0
        if nums[m] >= target:
            return m
        return m+1
