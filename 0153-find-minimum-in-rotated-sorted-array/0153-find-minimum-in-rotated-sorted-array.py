class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            print(l, m, r)

            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            elif nums[l] > nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return m