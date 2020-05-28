import sys
def minCoinExchangeProblem(S,m,value):
    dp=[0 for x in range(value+1)]
    dp[0]=0
    for i in range(1, value+1):
        dp[i]=sys.maxsize
    for i in range(1,value+1):
        for j in range(m):
            if S[j]<=i:
                sub_res=dp[i-S[j]]
                if sub_res!=sys.maxsize and sub_res+1<dp[i]:
                    dp[i]=sub_res+1
    return dp[value]

coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print(minCoinExchangeProblem(coins,m,V))

