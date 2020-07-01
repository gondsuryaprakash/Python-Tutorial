def count(s,k):
    res=0
    cnt = [0] * 27
    for i in range(len(s)):
        dist_count = 0
        for j in range(i,len(s)):
            if cnt[ord(s[j]) - 97] == 0:
                cnt[ord(s[j]) - 97] += 1
                dist_count += 1
            cnt[ord(s[j]) - 97] += 1
            if dist_count == k:
                res += 1

    return res

t=int(input())
for _ in range(t):
    s=input()
    k=int(input())
    res=count(s,k)
    print(res)
