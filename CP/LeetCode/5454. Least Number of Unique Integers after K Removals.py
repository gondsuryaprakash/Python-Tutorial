def removing(arr,k):
    hashMap={}
    for i in range(len(arr)):
        if arr[i] not in hashMap:
            hashMap[arr[i]]=1
        else:
            hashMap[arr[i]]+=1


    print(kerArr)

    print(hashMap)
arr=[4,3,1,1,3,3,2]
k=1
removing(arr,k)

