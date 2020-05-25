class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(tmp):
    if not tmp:
        return
    inorder(tmp.left)
    print(tmp.data,end=' ')
    inorder(tmp.right)

def deletDeepest(root,d_node):
    q=[]
    q.append(root)
    while len(q):
        tmp=q.pop(0)
        if tmp is d_node:
            tmp=None
            return
        if tmp.right:
            if tmp.right is d_node:
                tmp.right=None
                return
            else:

                q.append(tmp.right)
        if tmp.left:
            if tmp.left is d_node:
                tmp.left=None
                return
            else:
                q.append(tmp.left)

def deletion(root,key):
    if root==None:
        return None
    if root.left==None and root.right==None:
        if root.key==key:
            return None
        else:
            return root
        key_Node=None
        q=[]
        q.append(root)
        while len(q):
            tmp=q.pop(0)
            if tmp.data==key:
                key_node=tmp
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        if key_node:
            x=tmp.data
            deletDeepest(root,tmp)
            key_node.data=x
        return root




