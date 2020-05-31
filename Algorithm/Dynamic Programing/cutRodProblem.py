INT_MIN=-32767
def cutRod(price,n):
    dp=[0 for x in range(n+1)]
    dp[0]=0
    for i in range(1,n+1):
        max_value=INT_MIN
        for j in range(i):
            max_value=max(max_value,price[j]+dp[i-j-1])
        dp[i]=max_value
    return dp[n]
arr = [1, 5, 8, 9, 10, 17, 17, 20]
n=len(arr)
print(cutRod(arr,n))


