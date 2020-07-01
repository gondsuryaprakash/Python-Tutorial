def rint(list):
    return ''.join(list)
def permute(s,l,r,res):

    if l==r:
        res.append(rint(s))
    for i in range(l,r+1):
        s[l],s[i]=s[i],s[l]

        permute(s,l+1,r,res)
        s[l], s[i] = s[i], s[l]
t=int(input())
for _ in range(t):
    s=input()
    s=list(s)
    res=[]

    permute(s,0,len(s)-1,res)
    res.sort()
    for i in res:
        print(i,end=" ")