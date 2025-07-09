class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        A = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums) - 1
            while l < r:
                val = nums[l] + nums[r] + nums[i]
                if val == 0:
                    A.add(tuple([nums[i], nums[l], nums[r]]))
                elif val < 0:
                    l+=1
                    continue
                r-=1
        return list(A)
