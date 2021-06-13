
# Dynamic Programming


#Standard
# Time: O(2^n)
# Space: O(N) - Depth of the stack
def fib(n):
    if n<=2:return 1
    return fib(n-1)+fib(n-2)


#Memorization
# Time: O(2N) = O(N)
# Space: O(N)
def fibMemo(n):
    memo = {1: 1, 2: 1}
    def helper(n):
        if n not in memo:
            memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]
    return helper(n)

#Tabulation
# Time: O(N)
# Space: O(N)
def fibTub(n):
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]


def main():
    n = 30
    print(fib(30))
    print(fibMemo(30))
    print(fibTub(30))

###############################
if __name__=="__main__":
    main()
