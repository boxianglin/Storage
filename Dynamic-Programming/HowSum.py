
# M = Target Sum, N = numbers.length
# Time: O(N^M * M) '*M because result list should be accumulates"
# Space: O(M)
def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None
    for cur in numbers:
        rem = targetSum - cur
        curList = howSum(rem,numbers)
        if curList is not None:
            result = curList + [cur]
            return result

    return None

# Time: O(N*M*M) :N*M recursive calls with *M of copy array, = O(N*M^2)
# Space: O(M*M) : M keys, a key with most M size of array
def howSumMemo(targetSum, numbers):
    memo = {}
    def helper(targetSum, numbers):
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return []
        if targetSum < 0: return None
        for cur in numbers:
            rem = targetSum - cur
            curList = helper(rem, numbers)
            if curList is not None:
                result = curList + [cur]
                memo[targetSum] = result
                return memo[targetSum]
        memo[targetSum] = None
        return None
    return helper(targetSum,numbers)

print('brute Force',howSum(7,[2,3]))
print('Memo',howSumMemo(7,[2,3]))
print(howSumMemo(300,[7,14]))