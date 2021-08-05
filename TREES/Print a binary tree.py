class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printDetailed(root):
    if root==None:
        return
    print(root.data,end=':')
    if root.left!=None:
        print("L",root.left.data,end=',')
    if root.right!=None:
        print("R",root.right.data,end=" ")
    print()
    printDetailed(root.left)
    printDetailed(root.right)



b1=Binarytree(1)
b2=Binarytree(2)
b3=Binarytree(3)
b4=Binarytree(4)
b5=Binarytree(5)

b1.left=b2
b1.right=b3
b2.left=b4
b2.right=b5

printTree(b1)
printDetailed(b1)
