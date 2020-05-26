def binomilCoefficent(n,k):
    if k==0 or k==n:
        return 1
    return binomilCoefficent(n - 1, k - 1) + binomilCoefficent(n - 1, k)

print(binomilCoefficent(5,2))