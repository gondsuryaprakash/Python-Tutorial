def binarySearch(arr,l,r,key):
    if r>=1:
        mid=l+(r-l)//2
        if arr[mid]==key:
            return 1
        elif arr[mid]>key:
            return binarySearch(arr,l,mid-1,key)
        else:
            return binarySearch(arr,mid+1,r,key)
    else:
        return -1

t=int(input())
for i in range(t):
    n,key=map(int,input().split())
    arr=list(map(int,input().split()))
    ind=binarySearch(arr,0,n-1,key)
    print(ind)
