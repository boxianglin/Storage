from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        digitlst = [char for char in digits]
        pair1 = memo[digitlst[0]]
        pair2 = memo[digitlst[1]]
        res = []
        for c1 in pair1:
            for c2 in pair2:
                res.append(c1+c2)
        return res