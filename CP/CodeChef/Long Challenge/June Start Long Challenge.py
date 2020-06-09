t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    initialsum=sum(arr)
    for i in range(n):
        if arr[i]>k:
            arr[i]=k
    lateSum=sum(arr)
    diff=initialsum-lateSum
    print(diff)
