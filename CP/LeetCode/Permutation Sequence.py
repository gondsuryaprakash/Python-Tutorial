def permutation(n):
    if n==0 or n==1:
        return 1
    else:
        return n*permutation(n-1)

def nthPerm(n):
    arr=[0 for i in range(permutation(n))]
    for i in range(n):
        for j in range(n):
            if i!=j:
                str="{}{}"


