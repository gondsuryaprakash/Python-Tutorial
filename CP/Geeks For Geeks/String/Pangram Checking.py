def panagramCheck(s):
    s=s.lower()

    flag=0
    arr=[0 for i in range(26)]
    for i in range(len(s)):
        if s[i].isalpha():
            arr[ord(s[i]) - 97] = 1
    for el in arr:
        if el==0:
            flag=1
            break
    return True if flag==0 else False

a=panagramCheck("Bawds jog, flick quartz, vex nymph")
print(a)