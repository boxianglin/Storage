from typing import List

# a^b^a = a^a^b = (0)^b = b
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n) run time, O(1) space
        repeat = 0
        for num in nums:
            repeat = repeat^num
        return repeat

# [4,1,2,1,2]
# 4: 100
# 1: 001
# 2: 010
########################
# 1) 100 xor 000 = 100
# 2) 100 xor 001 = 101
# 3) 101 xor 010 = 111
# 4) 111 xor 001 = 110
# 5) 110 xor 010 = 100 = 4
