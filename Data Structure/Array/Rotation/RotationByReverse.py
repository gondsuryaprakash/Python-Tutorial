def reverseArray(arr,start,end):
    while start<end:
        tmp=arr[start]
        arr[start]=arr[end]
        arr[end]=tmp
        start+=1
        end-=1


def rotateArray(arr,d,n):
    reverseArray(arr,0,d)
    reverseArray(arr,d+1,n-1)
    reverseArray(arr,0,n-1)
    print(arr)

rotateArray([1,2,3,4,5],2,5)