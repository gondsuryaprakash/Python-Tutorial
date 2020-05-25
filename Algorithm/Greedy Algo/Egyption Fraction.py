import math
def egyption(nr,dr):
    ef=[]

    while nr!=0:
        x=math.ceil(dr/nr)
        ef.append(x)
        nr=x*nr-dr
        dr=x*dr

    for i in range(len(ef)):
        if i!=len(ef)-1:
            print("1/{0} +".format(ef[i]),end=" ")
        else:
            print("1/{0}".format(ef[i]), end=" ")


egyption(6,14)
