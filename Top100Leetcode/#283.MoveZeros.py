from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = slow pointer, j = fast pointer
        # i<=j, i+x=j, where among the x range, [i+x] = 0
        # i++ for each swap when [j] != 0 is safe
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1
