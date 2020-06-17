class Node:
    def __int__(self,data):
        self.data=data
        self.left=None
        self.right=None



def height(node):
    if node is None:
        return
    return 1+max(height(node.left),height(node.right))


def diameter(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)
    ldiameter=diameter(root.left)
    rdiameter=diameter(root.right)
    return max(lheight+rheight+1,max(rdiameter,ldiameter))