def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]



t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    bubbleSort(arr)
    print(arr)
