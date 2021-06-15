
# Time: O(N^M * M) N^M calls but * M because each suffix computed each call
# Space: O(M^2)
def canConstruct(target, wordBank):
    #1 Base case that returns TRUE
    if target == "": return True
    for word in wordBank:
        # ex. target = abc, word = ab then [:len(word)] = ab
        if len(target) >= len(word) and target[:len(word)] == word:
            suffix = target[len(word):]
            if canConstruct(suffix,wordBank):
                return True
    return False

# Time: O(N*M^2) M^2 = M keys * M subString Operations * N branches
# Space: O(M^2)
def canConstructMemo(target,wordBank):
    memo = {}
    def helper(target,wordbank):
        if target in memo: return memo[target]
        if target == "": return True
        for word in wordBank:
            # ex. target = abc, word = ab then [:len(word)] = ab
            if len(target) >= len(word) and target[:len(word)] == word:
                suffix = target[len(word):]
                if helper(suffix, wordBank):
                    memo[target] = True
                    return True
        memo[target] = False
        return False
    return helper(target,wordBank)

def canConsturctIte(target,wordBank):
    table = [False]*(len(target)+1)
    table[0] = True
    for i in range(len(target)):
        if table[i] is True:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[len(target)]

print(canConstruct("abcdef", ["ab","abc","cd","def","abcd"])) #true
print(canConstructMemo("abcdef", ["ab","abc","cd","def","abcd"])) #true
print(canConsturctIte("abcdef", ["ab","abc","cd","def","abcd"])) #true