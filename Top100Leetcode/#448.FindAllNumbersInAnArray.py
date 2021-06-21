from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        table = [False] * (len(nums) + 1)
        for i in range(len(nums)):
            index = nums[i]
            table[index] = True

        nums = [i for i in range(1,len(table)) if table[i] is False]
        return nums

# set differences
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set([i for i in range(1,len(nums)+1)])
        b = set(nums)
        return list(a-b)

# using negative as a sign for existence
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            exist = abs(nums[i]) - 1
            nums[exist] = abs(nums[exist]) * -1

        res = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return res