def findLargest(arr,n):
    arr.sort()
    divCount=[1 for i in range(n)]
    prev=[-1 for i in range(n)]
    max_index=0
    for i in range(1,n):
        for j in range(i):
            if arr[i]%arr[j]==0:
                if divCount[i] < divCount[j] + 1:
                    divCount[i] = divCount[j] + 1
                    prev[i]=j
        if divCount[max_index]<divCount[i]:
            max_index=i
    k=max_index
    res=[]
    while k>=0:
        res.append(arr[k])
        k=prev[k]
    return res

arr=[1,2,3]
res=findLargest(arr,3)
res=res[::-1]










