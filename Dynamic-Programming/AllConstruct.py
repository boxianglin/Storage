
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

def allconstructIte(target, wordBank):
    table = [[] for i in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                new_combinations = [combination + [word] for combination in table[i]]
                print(table[i+len(word)],'---',new_combinations)
                table[i + len(word)].extend(new_combinations)
    return table[len(target)]

# print(allconstruct("purple",["purp","p","ur","le","purpl"]))
# print(allconstructMemo("purple",["purp","p","ur","le","purpl"]))
print('result:',allconstructIte("purple",["purp","p","ur","le","purpl"]))
a = [[['purp']]]
b = [['p', 'ur', 'p']]
a[0].extend(b)
print(a[0])

