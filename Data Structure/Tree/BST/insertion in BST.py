class Node:
    def __int__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,node):
    if root is None:
        root=node
    if node.data<root.data:
        if root.left is None:
            root.left=node
        else:
            insert(root.left,node)
    if node.data>root.data:
        if root.right is None:
            root.right=node
        else:
            insert(root.right,node)
    return root
def minValueNode(node):
    current=node
    while current.left is not None:
        current=current.left
    return current
def getMax(node):
    current=node
    while current.right is not None:
        current=current.right
    return current
def deletNode(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=deletNode(root.left,key)
    elif key>root.key:
        root.right=deletNode(root.right,key)
    else:
        if root.left is None:
            tmp=root.right
            root=None
            return tmp
        elif root.right is None:
            tmp=root.left
            root=None
            return tmp
        tmp=minValueNode(root.right)
        root.data=tmp.data
        root.right=deletNode(root.right,tmp.data)
    return root

