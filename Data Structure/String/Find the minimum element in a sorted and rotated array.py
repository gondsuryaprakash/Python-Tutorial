def findMin(arr,l,h):
    if h<l:
        return arr[0]
    if h==l:
        return arr[l]
    mid=int((l+h)/2)
    if mid<h and arr[mid+1]<arr[mid]:
        return arr[mid+1]
    if mid > l and arr[mid]<arr[mid-1]:
        return arr[mid]
    if arr[h]>arr[mid]:
        return findMin(arr,l,mid-1)
    return findMin(arr,mid+1,h)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(findMin(arr,0,n-1))
