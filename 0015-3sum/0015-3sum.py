class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        B = set()
        C = set()
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                val = -1 * nums[i]
                if val - nums[j] in B:
                    C.add(tuple(sorted([nums[i], nums[j], val - nums[j]])))
                B.add(nums[j])
            B.clear()
        return list(C)
