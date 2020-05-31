def cyclicRotation(arr,n):
    tmp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=tmp
    return arr
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    res=cyclicRotation(arr,n)
    for el in res:
        print(el,end=" ")
    print()
