def removeDuplicateUptoTwo(arr):
     hashmap={}
     a=[]
     for i in range(len(arr)):
          if arr[i] not in hashmap:
               hashmap[arr[i]]=0
               a.append(arr[i])
          else:
               if hashmap[arr[i]]<1:
                    a.append(arr[i])
                    hashmap[arr[i]]+=1
     a.sort()
     return a



a=removeDuplicateUptoTwo([1,1,1,1,2,2,2,3,3,3,5,6,7,8,4,2,1])
print(a)








