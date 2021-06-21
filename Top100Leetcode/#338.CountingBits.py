from typing import List


# offest to the corresponding prev bit + 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 0
        for i in range(1,n+1):
            if i & (i-1) == 0: offset = i
            dp[i] = dp[i-offset] + 1
        return dp

# x = x/2 + 1(odd) or 0 (even)
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i>>1] + i%2
        return dp

# x & (x-1) + 1 always get the answer
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        for i in range(1,n+1):
            y = i & (i-1)
            dp[i] = dp[y] + 1
        return dp