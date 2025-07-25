class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P = [1] * len(nums)
        S = [1] * len(nums)
        p, s = 1, 1

        for i in range(len(nums) - 1):
            p *= nums[i]
            P[i + 1] = p
        
        for i in reversed(range(len(nums) - 1)):
            s *= nums[i + 1]
            S[i] = s
        
        return [P[i] * S[i] for i in range(len(nums))]