t=int(input())
for i in range(t):
    str=input()
    count=0
    i=0
    while i<len(str)-1:
        if str[i]!=str[i+1]:
            count+=1
            i+=1
        i+=1
    print(count)