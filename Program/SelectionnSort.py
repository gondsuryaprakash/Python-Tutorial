def selectionSort(list):
    for i in range(0,len(list)-1):
        minValueIndex=i
        for j in range(i+1,len(list)):
            if list[minValueIndex]>list[j]:
                minValueIndex=j
        tempValue=list[i]
        list[i]=list[minValueIndex]
        list[minValueIndex]=tempValue

list=[12,34,5,55,33,4]
selectionSort(list)
print(list)
