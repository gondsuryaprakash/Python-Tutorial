t=int(input())
for i in range(t):
    arr=list(map(int,(input().split())))
    p=arr[-1]
    n=len(arr)
    sum=0
    for i in range(0,n-1):
        sum+=arr[i]*p

    if sum<=(24*5):
        print("No")
    else:
        print("Yes")

