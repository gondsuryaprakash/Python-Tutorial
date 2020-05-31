def modulartSum(arr,n,m):
    if n>m:
        return True
    dp=[False for i in range(m)]
    for i in range(n):
        if dp[0]:
            return True
        tmp=[False for i in range(m)]
        for j in range(m):
            if dp[j]==True:
                if dp[(j+arr[i])%m]==False:
                    tmp[(j+arr[i])%m]=True
        for j in range(m):
            if tmp[j]:
                dp[j]=True

        dp[arr[i]%m]=True
    return dp[0]



arr = [1, 7]
n = len(arr)
m = 5

a=modulartSum(arr,n,m)
print(a)
