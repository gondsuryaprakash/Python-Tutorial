a=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
b=sorted(a,key=lambda a:(-a[0] ,a[0]))
c=[]
for i in b:
    print(c)
    print(i[1],i)

    c.insert(i[1],i)

print(b)
