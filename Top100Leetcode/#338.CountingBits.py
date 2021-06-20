from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        num = 0
        res = []
        while num <= n:
            bnum = str(format(num, "b"))
            print(bnum)
            count = 0;
            for d in bnum:
                if d == '1': count += 1
            res.append(count)
            num += 1
        return res
