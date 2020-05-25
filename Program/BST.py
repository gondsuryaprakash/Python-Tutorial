class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def insert(root,node):
    if root is None:
        root=node
        return root
    if node.value<root.value:
        root.left=insert(root.left,node)
    if node.value>root.value:
        root.right=insert(root.right,node)
    return root
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
def getMinValue(root):
    if root:
        while root.left is not  None:
            root=root.left
        return root
def deletNode(root,value):
    if root is None:
        return  root
    if value<root.value:
        root.left=deletNode(root.left,value)
    elif value> root.value:
        root.right=deletNode(root.right,value)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        else:
            temp=getMinValue(root.right)
            root.value=temp.value
            root.right=deletNode(root.right,temp.value)
    return root


root=Node(50)
insert(root,Node(10))
insert(root,Node(2))
insert(root,Node(80))
insert(root,Node(15))
insert(root,Node(60))
insert(root,Node(90))
deletNode(root,50)
postorder(root)

