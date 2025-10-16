class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}

        for i, v in enumerate(nums):
            if target - v in val_idx:
                return [i, val_idx[target - v]]
            val_idx[v] = i