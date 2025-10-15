class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(subset, curr_sum, index):
            if curr_sum == target:
                res.append(subset.copy())
                return
            elif curr_sum > target:
                return

            for i in range(index, len(candidates)):
                subset.append(candidates[i])
                dfs(subset, curr_sum + candidates[i], i)
                subset.pop()

        dfs([], 0, 0)
        return res