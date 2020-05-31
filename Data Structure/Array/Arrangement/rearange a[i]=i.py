def Reaarrange(arr):
    s=set()
    for i in range(len(arr)):
        s.add(arr[i])
    for j in range(len(arr)):
        if j in s:
            arr[j]=j
        else:
            arr[j]=-1

    return arr

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    res=Reaarrange(arr)
    for el in res:
        print(el,end=" ")
    print()
