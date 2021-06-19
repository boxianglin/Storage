from typing import List

# General Approach O(nlogn) time, O(log n) space for stack calls
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# O(N) runtime, O(1) Space
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        count  = 0
        numHolder = None

        for num in nums:
            if count == 0:
                numHolder = num
            count += 1 if num == numHolder else -1
        return numHolder