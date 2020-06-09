class Node:
    def __int__(self,data):
        self.data=data
        self.left=None
        self.right=None
def iterativePreOrder(root):
    if root is None:
        return
    st=[]
    st.append(root)
    while len(st)!=0:
        node=st.pop()
        print(node.data)

        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)


def iterativeInOrder(root):
    current=root
    st=[]
    done=0
    res=[]
    while True:
        if current is not  None:
            st.append(current)
            current=current.next
        elif (st):
            current=st.pop()
            res.append(current.data)
            current=current.right

        else:
            break


