t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    arr=list(map(int,input().split()))
    n=n+1
    totalSum=n*(n+1)//2
    print(totalSum)
    for i in arr:
        totalSum-=i

    print(totalSum if totalSum>0 else -1 )
