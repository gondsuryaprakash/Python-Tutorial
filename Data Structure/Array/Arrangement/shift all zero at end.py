def shiftAllZero(arr,n):
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count += 1
    while count<n:
        arr[count]=0
        count+=1
    return arr
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    res=shiftAllZero(arr,n)
    for el in res:
        print(el,end=" ")
    print()


def moveZerosToEnd(arr, n):
    # Count of non-zero elements
    count = 0;

    # Traverse the array. If arr[i] is non-zero, then
    # swap the element at index 'count' with the
    # element at index 'i'
    for i in range(0, n):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count += 1