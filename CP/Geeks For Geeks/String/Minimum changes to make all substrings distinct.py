t=int(input())
for i in range(t):
    ch=[0]*26
    st=input()

    for i in st:
        ch[ord(i.lower())-97]+=1

    sum=0
    for i in range(26):
        if ch[i]>0:
            sum += ch[i] - 1

    print(sum)


