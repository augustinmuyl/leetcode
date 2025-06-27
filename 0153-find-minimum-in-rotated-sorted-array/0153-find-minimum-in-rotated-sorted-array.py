class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi, lo = len(nums)-1, 0
        val = nums[0]
        while (lo <= hi):
            if nums[lo] < nums[hi]:
                return min(nums[lo], val)
            mid = (hi+lo)//2
            val = min(val, nums[mid])
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1
        return val
        