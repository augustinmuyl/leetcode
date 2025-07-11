class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            print(m)
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return (l + r) // 2
