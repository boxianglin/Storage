
# TIME: O(N^M * M)
# Space: O(M^2)
def countConstruct(target,wordBank):
    if target == "": return 1
    total = 0
    for word in wordBank:
        # ex. target = abc, word = ab then [:len(word)] = ab
        if len(target) >= len(word) and target[:len(word)] == word:
            suffix = target[len(word):]
            count = countConstruct(suffix,wordBank)
            total = total + count
    return total


# TIME: O(N * M^2)
# Space: O(M^2)
def countConsturctMemo(target,wordBank):
    memo = {}
    def helper(target,wordBank):
        if target in memo: return memo[target]
        if target == "": return 1
        total = 0
        for word in wordBank:
            # ex. target = abc, word = ab then [:len(word)] = ab
            if len(target) >= len(word) and target[:len(word)] == word:
                suffix = target[len(word):]
                count = countConstruct(suffix, wordBank)
                total = total + count
        memo[target] = total
        return total
    return helper(target,wordBank)


def CountConstructIte(target, wordBank):
    table = [0]*(len(target)+1)
    table[0] = 1
    for i in range(len(target)):
        if table[i] >= 1:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] += table[i]
    return table[len(target)]


print(countConstruct("purple", ["purp","p","ur","le","purpl"])) #2
print(countConsturctMemo("purple", ["purp","p","ur","le","purpl"])) #2
print(CountConstructIte("purple", ["purp","p","ur","le","purpl"])) #2