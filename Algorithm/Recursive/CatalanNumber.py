def catalan(n):
    if n<=1:
        return n
    res=0
    for i in range(n):
        res+=catalan(i)*catalan(n-i-1)
    return res
