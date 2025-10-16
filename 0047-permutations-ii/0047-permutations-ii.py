class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in count:
                if count[i] < 1:
                    continue
                subset.append(i)
                count[i] -= 1
                dfs(subset)
                count[subset.pop()] += 1

        dfs([])
        return res