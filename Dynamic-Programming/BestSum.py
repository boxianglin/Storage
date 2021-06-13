

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


print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))

