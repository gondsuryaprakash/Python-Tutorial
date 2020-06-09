t=int(input())
for i in range(t):
    res=[0]*26
    res1=[0]*26
    str=input()
    mid=len(str)//2
    if len(str)%2==1:
        half=str[:len(str)//2]
        bad=str[len(str)//2+1:]
    else:
        half=str[:len(str)//2]
        bad=str[len(str)//2:]
    for i in half:
        res[ord(i.lower())-97]+=1
    for j in bad:
        res1[ord(j.lower())-97]+=1
    print("YES" if res==res1 else "NO")
    print()






