class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while True:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                return nums[l]