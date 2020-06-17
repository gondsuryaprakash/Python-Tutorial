import numpy as np

d={}
def coin(x):
    if x<12:
        return x
    if x not in d:
        d[x]=coin(x//2)+coin(x//3)+coin(x//4)
    return d[x]

i=0
while i<=10:
    n=int(input())
    if n=='':
        break
    print(coin(n))


