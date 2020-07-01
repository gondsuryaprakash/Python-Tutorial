import math
def search(arr,k,l,r):
    arr.sort()
    if r>=1:
        mid=(r+(r-l))//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return search(arr,k,mid+1,r)
        else:
            return search(arr,k,l,mid-1)
    else:
        return -1

def primeFacctor(n,k):
    arr=[]
    while n%2==0:
        arr.append(2)
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            arr.append(i)
            n//=i
    if n>2:
        arr.append(n)
    if k>len(arr)-1:
        return -1
    return arr[k-1]


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    print(primeFacctor(n,k))












