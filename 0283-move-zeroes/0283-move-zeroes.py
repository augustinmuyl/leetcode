class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 1
        while (r < len(nums)):
            if nums[l] == 0:
                nums[l] = nums[r]
                nums[r] = 0
            if nums[l] != 0:
                l+=1
            r+=1
