def findSubsequennce(s,t,m,n):

    if m==0:
        return True
    if n==0:
        return False

    if s[m-1]==t[n-1]:
        return findSubsequennce(s, t,m-1,n-1)
    return findSubsequennce(s,t,m,n-1)


string1 = "gksrek"
string2 = "geeksforgeeks"
a=findSubsequennce(string1,string2,len(string1),len(string2))
print(a)