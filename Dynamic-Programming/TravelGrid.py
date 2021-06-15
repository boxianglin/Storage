# Begin at the top-left corner and travel down to the button-down
# Move only DOWN OR RIGHT, Compute numbers of way

    #             (2,3)
    #          D/       \R
    #         (1,3)       (2,2)
    #       /     \       /    \
    #     (0,3)   (1,2) (1,2)  (2,1)
    #            /    \   /    \   /  \
    #         (0,2)(1,1)(0,2)(1,1)(1,1)(0,0)

    # Base case 1. (0,M)|(N,0) = 0
    #           2. (M,N) where M=N = 1

# Time: O(2^(N+M)) Height: N+M
# Space: O(N+M)
def gridTravel(m,n):
    if(m==1 and n==1): return 1
    if(m==0 or n==0): return 0
    return gridTravel(m-1,n) + gridTravel(m,n-1)


#Memorization
# Time: O(M*N) in a sense of order don't matter combinations, but roughly, because key={m,n} not set equally with{n,m}
# Space: O(N+M)
def gridTravelMemo(m,n):
    memo = {}
    def helper(m,n):
        key = str(m) + ',' + str(n)
        if key in memo: return memo[key]
        if(m==0 or n==0): return 0
        if(m==1 and n==1): return 1
        memo[key] = helper(m-1,n) + helper(m,n-1)
        return memo[key]
    return helper(m,n)



#Iterative Method
#Time Spce O(MN)

def gridTravelIte(m,n):
    table = [[0]*(n+1) for row in range(m+1)]
    table[1][1] = 1
    for i in range(1,m):
        for j in range(1,n):
            cur = table[i][j]
            table[i+1][j] += cur
            table[i][j + 1] += cur

    # right column
    for i in range(1, m):
        table[i + 1][n] += table[i][n]
    # bottom row
    for j in range(1, n):
        table[m][j + 1] += table[m][j]
    return table[m][n]



def main():
    #print(gridTravel(3,2))
    # print(gridTravelMemo(3,2))
    print(gridTravelIte(3,2))



###############################
if __name__=="__main__":
    main()