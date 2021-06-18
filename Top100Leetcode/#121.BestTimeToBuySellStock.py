from typing import List

# i to i_(n), a continuous sequence, i_(m) where i <= m <= n is min, then i - i_(m) makes profits
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for p in prices:
            minPrice = min(p, minPrice)
            curProfit = p - minPrice
            if curProfit > profit: profit = curProfit
        return profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))