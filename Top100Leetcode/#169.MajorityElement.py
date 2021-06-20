import random
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

# ideally O(N) runtime O(1) space
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(i, j):
            if i == j: return nums[i]
            mid = (i + j) // 2
            leftMajor = helper(i, mid)
            rightMajor = helper(mid + 1, j)

            if leftMajor == rightMajor: return leftMajor

            leftCount = sum(1 for i in range(i, j + 1) if nums[i] == leftMajor)
            rightCount = sum(1 for i in range(i, j + 1) if nums[i] == rightMajor)

            return leftMajor if leftCount > rightCount else rightMajor

        return helper(0, len(nums) - 1)

