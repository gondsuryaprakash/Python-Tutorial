def searchAndInsert(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        else:
            return insertAt(arr,target)

def insertAt(arr,target):
    if target>max(arr):
        return len(arr)
    if target<min(arr):
        return 0
    for i in range(len(arr)-1):
        if arr[i]<=target and arr[i+1]>=target:
            return i+1

