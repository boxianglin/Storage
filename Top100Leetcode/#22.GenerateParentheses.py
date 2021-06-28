class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(cur_str, left, right):

            if right > left: return
            if left == n and right == n: res.append(cur_str)
            if left < n: dfs(cur_str + '(', left + 1, right)
            if right < n: dfs(cur_str + ')', left, right + 1)

        cur_str = ''
        res = []
        dfs(cur_str, 0, 0)
        return res