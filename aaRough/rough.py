def divisibilityof11(s):
    s1 = 0
    s2 = 0
    for i in range(len(s)):
        if i%2==0:
            s1+=int(s[i])
        else:
            s2+=int(s[i])
    return 1 if (s1-s2)%11==0 else 0

t=int(input())
for _ in range(t):
    s=input()
    print(divisibilityof11(s))












