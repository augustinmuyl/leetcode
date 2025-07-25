class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P = [None] * len(nums)
        S = [None] * len(nums)
        p, s = 1, 1

        for i in range(len(nums) - 1):
            p *= nums[i]
            P[i + 1] = p
        
        for i in reversed(range(len(nums) - 1)):
            s *= nums[i + 1]
            S[i] = s
        
        return [P[i] * S[i] if P[i] is not None and S[i] is not None else P[i] if S[i] is None else S[i] for i in range(len(nums))]