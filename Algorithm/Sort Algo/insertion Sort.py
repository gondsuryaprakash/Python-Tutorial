def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key


t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    insertion(arr)
    print(arr)