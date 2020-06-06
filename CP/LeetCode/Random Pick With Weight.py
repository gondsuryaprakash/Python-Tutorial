def sortStack(s):
    st=[]
    while len(s)!=0:
        tmp=s[-1]
        s.pop()
        while len(st)!=0 and tmp<st[-1]:
            s.append(st[-1])
            st.pop()
        else:
            st.append(tmp)
