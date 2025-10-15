class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(subset, curr_sum, i):
            if curr_sum == target:
                res.append(subset.copy())
                return
            elif i >= len(candidates) or curr_sum > target:
                return

            subset.append(candidates[i])
            dfs(subset, curr_sum + candidates[i], i + 1)
            subset.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(subset, curr_sum, j)

        dfs([], 0, 0)
        return res