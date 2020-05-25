def insertionSort(list):
    for i in range(1,len(list)):
        value=list[i]
        j=i
        while(j>0 and list[j-1]>value):
            list[j]=list[j-1]
            j=j-1
        list[j]=value
list=[29,32,11,34]
insertionSort(list)
print(list)

