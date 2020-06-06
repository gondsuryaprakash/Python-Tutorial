def nextGreater(arr):
    st=[0]
    st[0]=arr[0]
    dics={}
    for i in range(1,len(arr)):
        while len(st)>0 and arr[i]>st[0]:
            dics[st[0]]=arr[i]
            st.pop(0)
        else:
            st.insert(0,arr[i])
    while len(st):
        dics[st[0]] = -1
        st.pop(0)

    for el in arr:
        print(dics[el],end=" ")


t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    nextGreater(arr)



    # while len(st)!=0:
    #     top=st.pop(0)
    #     print(top)
    #     st.pop(0)
    # print(-1)


