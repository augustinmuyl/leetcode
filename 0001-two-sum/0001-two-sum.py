class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}

        for i, v in enumerate(nums):
            if target - v in A:
                return [i, A[target - v]]
            A.update({v: i})
        