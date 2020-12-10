class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



def insert(root, node):
    if root == None:
        root = node
    elif root.data > node.data:
        if root.left == None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right == None:
            root.right = node
        else:
            insert(root.right, node)

def preoder_print(node):
    if node == None:
        return None
    else:
        print(node.data)
        if node.left:
            preoder_print(node.left)
        if node.right:
            preoder_print(node.right)

r = Node(3)
insert(r, Node(7))
insert(r, Node(1))
insert(r, Node(5))
preoder_print(r)
