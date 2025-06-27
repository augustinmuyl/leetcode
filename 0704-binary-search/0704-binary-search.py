class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi, lo = len(nums), 0
        while (lo < hi):
            mid = (hi+lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return -1
