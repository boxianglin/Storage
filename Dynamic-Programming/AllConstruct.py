
#Time: O(N^M)
#Space: O(M)
def allconstruct(target, wordBank):
    if target == "": return [[]]
    result = []
    for word in wordBank:
        if len(target) >= len(word) and target[:len(word)] == word:
            suffix = target[len(word):]
            suffix_ways = allconstruct(suffix,wordBank)
            target_ways = [way+[word] for way in suffix_ways]
            result.extend(target_ways)
    return result

#Time: O(N^M)
#Space: O(M)
def allconstructMemo(target, wordBank):
    memo = {}
    def helper(target,wordBank):
        if target in memo: return memo[target]
        if target == "": return [[]]
        result = []
        for word in wordBank:
            if len(target) >= len(word) and target[:len(word)] == word:
                suffix = target[len(word):]
                suffix_ways = helper(suffix, wordBank)
                target_ways = [way + [word] for way in suffix_ways]
                result.extend(target_ways)
        memo[target] = result
        return result
    return helper(target,wordBank)


print(allconstruct("purple",["purp","p","ur","le","purpl"]))
print(allconstructMemo("purple",["purp","p","ur","le","purpl"]))