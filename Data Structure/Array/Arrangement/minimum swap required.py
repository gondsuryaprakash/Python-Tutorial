def minSwap(arr,n,k):
    count=0
    for i in range(0,n):
        if arr[i]<=k:
            count+=1
    bad=0
    for i in range(0,count):
        if arr[i]>k:
            bad+=1
    ans=bad
    j=count
    for i in range(0,n):
        if j==n:
            break
        if arr[i]>k:
            bad-=1
        if arr[j]>k:
            bad+=1
        ans=min(bad,ans)
        j+=1
    return ans

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    print(minSwap(arr,n,k))
