class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        
        for i, n in enumerate(nums):
            if (target - n) in A:
                return [A[target - n], i]
            A.update({n: i})
