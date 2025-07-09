class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        A = set()
        
        for i in range(len(nums)-2):
            l, r = i+1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while l < r:
                val = nums[l] + nums[r] + nums[i]
                if val == 0:
                    A.add(tuple([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1
                elif val < 0:
                    l+=1
                    continue
                else:
                    r-=1
        
        return list(A)
