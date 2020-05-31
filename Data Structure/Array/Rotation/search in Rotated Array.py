def binarySearch(arr,left,right,key):
    if right>=left:

        mid=(left+right)//2
        if key==arr[mid]:
            return mid
        elif key<arr[mid]:
            return binarySearch(arr,left,mid-1,key)
        else:
            return binarySearch(arr,mid+1,right,key)
    else:
        return -1


def pivoteBinarySearch(arr,n,key):
    pivot=findPivot(arr,0,n-1)
    if pivot==-1:
        return binarySearch(arr,0,n-1,key)
    if arr[pivot]==key:
        return pivot
    if arr[0]<=key:
        return binarySearch(arr,0,pivot-1,key)
    return binarySearch(arr,pivot+1,n-1,key)


def findPivot(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

        # low + (high - low)/2;
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    key=int(input())
    res=pivoteBinarySearch(arr,n,key)
    print(res)