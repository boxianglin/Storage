class Solution:
    def isValid(self,s: str) -> bool:
        stack = []
        memo = {")": "(", "}": "{", "]": "["}
        for p in s:
            if p in memo.keys():
                pair = memo.get(p)
                if stack != [] and pair == stack[-1]:
                    stack.pop()
                # Else when close parenthese passing in when stack empty, return False
                else:
                    return False
            # Else if not close parenthese we keep append
            else:
                stack.append(p)

        return stack == []

solution = Solution()
print(solution.isValid("([)]")) #False


