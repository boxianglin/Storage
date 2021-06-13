# takes in canSum(targetSum,numbers[]), return a boolean if elements in
# numbers[] able to = targetSum, note: elements are reusable
# assume non-negative numbers

# ex1. canSum(7,[5,3,4,7])
#          T OR F
#            7
# /       /    \       \   (-5, -3,-4,-7)
# 2       4     3       0
#        / \    |
#       1   0   0
# Time: O(n^m) where n = numbers[], and m = target sum,
# assuming height is m worst decreasing 1 per level, nodes are 1*n*n*n(for m_th).
# Space: O(m)
def canSum(targetSum, numbers):
    if targetSum == 0: return True
    if targetSum < 0: return False
    for cur in numbers:
        remainder = targetSum - cur
        # second level of tree from TragetSum Node,if one of the branch(path) is true then return true
        if canSum(remainder, numbers) :
            return True

    return False

# Time: O(m*n)
# Space: O(m)
def canSumMemo(targetSum, numbers):
    memo = {}
    def helper(targetSum,numbers):
        if targetSum in memo: return memo[targetSum]
        if targetSum == 0: return True
        if targetSum < 0: return False
        for cur in numbers:
            remainder = targetSum - cur
            # second level of tree from TragetSum Node,if one of the branch(path) is true then return true
            if helper(remainder, numbers):
                #memo[targetSum] = True
                return True

        # KEY STEP: when backtracking
        memo[targetSum] = False
        return False
    return helper(targetSum,numbers)


def main():
    print(canSum(7, (2, 3)))  # true
    print(canSum(7, (5, 3, 4, 7)))  # true
    print(canSum(7, (2, 4)))  # false
    print(canSum(8, (2, 3, 5)))  # true
  #  print(canSum(300, (7, 14)))  # false
    print('--------------')
    # print(canSumMemo(7, (2, 3)))  # true
    # print(canSumMemo(7, (5, 3, 4, 7)))  # true
    print(canSumMemo(7, (2, 4)))  # false
    # print(canSumMemo(8, (2, 3, 5)))  # true
    # print(canSumMemo(300, (7, 14)))  # false

###############################
if __name__ == "__main__":
    main()
