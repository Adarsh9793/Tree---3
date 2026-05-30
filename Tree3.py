

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def preorder(currNode):
    if currNode == None:
        return
    

    print(currNode.data, end=' ')
    preorder(currNode.left)
    preorder(currNode.right)


def inorder(currNode):
    if currNode == None:
        return
    

    inorder(currNode.left)
    
    print(currNode.data, end=' ')
    inorder(currNode.right)


def postorder(currNode):
    if currNode == None:
        return
    

    postorder(currNode.left)
    postorder(currNode.right)
    
    print(currNode.data, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

inorder(root)