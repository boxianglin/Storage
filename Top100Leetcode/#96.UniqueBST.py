class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        # dp[0] = 1, dp[1] = 1 dp[2] = 2
        for i in range(2,n+1):
            total = 0
            for cur in range(1,i+1):
                left = cur - 1 # ---> go through left to right  0 1
                right = i - cur
                total += dp[left]*dp[right]
            dp[i] = total
        return dp[n]


def numTrees(self, n: int) -> int:
    memo = {}

    def counter(start, end):
        if start < 1 or end > n or start >= end: return 1
        if (start, end) in memo:
            return memo[(start, end)]
        else:
            count = 0
            for i in range(start, end + 1):
                left = counter(start, i - 1)
                right = counter(i + 1, end)
                count += left * right
            memo[(start, end)] = count
        return count

    return counter(1, n)


class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def counter(n):
            if n <= 1: return 1
            if n in memo: return memo[n]
            else:
                count = 0
                for i in range(0, n):#(0,n-1)
                    count += counter(i) * counter(n-1-i)  #(0,n-1) (1,n-2) (2,n-3) subtrees
                memo[n] = count
                return count
        return counter(n)