def count(S,m,n):
    dp=[0 for k in range(n+1)]
    dp[0]=1
    for i in range(0,m):
        for j in range(S[i],n+1):
            dp[j]+=dp[j-S[i]]
    return dp[n]


a=[1,2,3]
m=len(a)
n=4
print(count(a,m,n))