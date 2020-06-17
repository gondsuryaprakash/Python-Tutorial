class Node:
    def __int__(self,data):
        self.data=data
        self.left=None
        self.right=None
def getMaxWidth(root):
    maxWidth=0
    if root is None:
        return 0
    h=height(root)
    for i in range(1,h+1):
        width=getWidth(root,i)
        if width>maxWidth:
            maxWidth=width
    return maxWidth


def height(node):
    if node is None:
        return 0
    return 1+max(height(node.left),height(node.right))
def getWidth(node,level):
    if node in None:
        return
    if level==1:
        return 1
    elif level>1:
        return getWidth(node.left, level - 1) + getWidth(node.right, level - 1)

