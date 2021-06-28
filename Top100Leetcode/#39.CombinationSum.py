from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(1,target+1):
                if i < c: continue
                if i == c: dp[i].append([c])
                if i > c:
                    for sublist in dp[i-c]:
                        dp[i].append(sublist+[c])
        return dp[target]
s = Solution()
print(s.combinationSum([2,3,6,7],7))


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(candidates, target, one_solution, start):

            if target < 0: return
            if target == 0:
                res.append(one_solution.copy())
                return

            for i in range(start, len(candidates)):
                one_solution.append(candidates[i])
                rem = target - candidates[i]
                backtrack(candidates, rem, one_solution, i)
                one_solution.pop()

        backtrack(candidates, target, [], 0)
        return res
s2 = Solution2()
print(s2.combinationSum([2,3,6,7],7))


class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, one_solution, cur_value):
            if cur_value < 0 or i >= len(candidates): return
            if cur_value == 0:
                res.append(one_solution.copy())
                return
            one_solution.append(candidates[i])
            dfs(i, one_solution, cur_value - candidates[i])
            one_solution.pop()
            dfs(i+1, one_solution, cur_value)
        dfs(0,[],target)
        return res