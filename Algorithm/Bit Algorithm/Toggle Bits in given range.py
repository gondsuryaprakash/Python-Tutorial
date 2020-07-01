def toggleBits(n,l,r):
    power=0
    mask=1
    val=0
    i=0
    while i<l:
        if mask&n:
            val+=pow(2,power)
        mask <<= 1
        power+=1
        i+=1
    while i<=r:
        if not(mask&n):
            val+=pow(2,power)
        mask <<=1
        power+=1
        i+1
    while i<10:
        if mask&n:
            val+=pow(2,power)
        mask <<= 1
        power+=1
        i+=1

    print(val)

toggleBits(50,2,5)


