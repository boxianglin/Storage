
# Time: O(N^M * M)
# Space: O(M*M) ：*M because shortest worst length.
def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    shortest = None
    for num in numbers:
        rem = targetSum - num
        curList = bestSum(rem,numbers)
        if curList is not None:
            curList = curList + [num]
            if shortest is None or len(curList) < len(shortest):
                shortest = curList.copy()

    return shortest


# Time: O(M*N*M)
# Space: O(M^2)
def bestSumMemo(targetSum, numbers):
    memo = {}
    def helper(targetSum, numbers):
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return []
        if targetSum < 0: return None
        shortest = None
        for num in numbers:
            rem = targetSum - num
            curList = helper(rem,numbers)
            if curList is not None:
                curList = curList + [num]
                if shortest is None or len(curList) < len(shortest):
                    shortest = curList.copy()
        memo[targetSum] = shortest
        return shortest
    return helper(targetSum,numbers)
#
# print(bestSum(7,[5,3,4,7]))
# print(bestSum(8,[2,3,5]))
# print(bestSumMemo(100,[1,2,5,25]))
print(bestSumMemo(8,[2,3,5]))

