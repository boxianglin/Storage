from typing import List

# Recursive Tree
# Call recursive inside of a for loop(level)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        memo = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        res = []

        def dfs(combination, digits):
            if not digits:
                res.append(combination)
            else:
                curDigit = digits[0]
                for letter in memo[curDigit]:
                    dfs(combination + letter, digits[1:])

        dfs('', digits)
        return res
