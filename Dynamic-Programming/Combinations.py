

def combinations(lst):
    result = list()
    def helper(i,path):
        if i == len(lst):
            result.append(path)
            return
        pwc = path.copy()
        pwc.append(lst[i])
        helper(i+1,path)
        helper(i+1,pwc)

    helper(0,[])
    print(result)

combinations([1,2,3])

