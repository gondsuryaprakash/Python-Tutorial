def countDIvisibility(str,n,m):
    l=m
    dp=[[0 for x in range(l)] for y in range(n)]
    dp[0][(ord(str[0])-ord('0'))%n]+=1
    for i in range(1,l):
        dp[i][(ord(str[i])-ord('0'))%n]+=1
        for j in range(n):
            dp[i][j]+=dp[i-1][j]
            dp[i][(j*10+(ord(str[i])-ord('0')))%n]+=dp[i-1][j]
    return dp[l-1][0]

t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    str=input()
    print(countDIvisibility(str, n,m))


