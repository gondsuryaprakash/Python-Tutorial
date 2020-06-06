def isoperand(exp):
    return exp.isalpha()
# postfix to infix
def infix(exp):
    s=[]
    for ex in exp:
        if isoperand(ex):
            s.insert(0,ex)
        else:
            op1=s[0]
            s.pop(0)
            op2=s[0]
            s.pop(0)
            str='('+op2+ex+op1+')'
            s.insert(0,str)

    return s[0]

exp = "ab*c+"
print(infix(exp.strip()))



