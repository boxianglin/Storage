from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalMax = nums[0];
        tempMax = 0;
        for num in nums:
            tempMax = max(tempMax+num, num)
            if tempMax > finalMax:
                finalMax = tempMax
        return finalMax

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6