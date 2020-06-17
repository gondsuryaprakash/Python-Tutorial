INT_MIN=-2**32
def check(pre):
    s=[]
    root=INT_MIN
    for val in pre:
        if val<root:
            return False
        while len(s)>0 and s[-1]<val:
            root=s.pop()

        s.append(val)
    return True


