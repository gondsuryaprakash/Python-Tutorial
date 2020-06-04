def kthlargest(arr,n,k):
    arr.sort(reverse=True)
    for i in range(0,k):
        print(arr[i],end=" ")
    print()

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    kthlargest(arr,n,k)
