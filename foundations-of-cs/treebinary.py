# p. 255

class BinaryTree:
    def __init__(self, nodeLabel, leftChild, rightChild):
        self.nodeLabel = nodeLabel
        self.leftChild = leftChild
        self.rightChild = rightChild

def preorder_binary_tree(tree):
    print("Preorder traversal of Binary Tree:  ", end="")
    preorder_binary_tree_traverse(tree)
    print()

def preorder_binary_tree_traverse(tree):
    if tree is not None:
        print(tree.nodeLabel, end=" ")
        preorder_binary_tree_traverse(tree.leftChild)
        preorder_binary_tree_traverse(tree.rightChild)
            
def inorder_binary_tree(tree):
    print("Inorder traversal of Binary Tree:   ", end="")
    inorder_binary_tree_traverse(tree)
    print()

def inorder_binary_tree_traverse(tree):
    if tree is not None:
        inorder_binary_tree_traverse(tree.leftChild)
        print(tree.nodeLabel, end=" ")
        inorder_binary_tree_traverse(tree.rightChild)

def postorder_binary_tree(tree):
    print("Postorder traversal of Binary Tree: ", end="")
    postorder_binary_tree_traverse(tree)
    print()

def postorder_binary_tree_traverse(tree):
    if tree is not None:
        postorder_binary_tree_traverse(tree.leftChild)
        postorder_binary_tree_traverse(tree.rightChild)
        print(tree.nodeLabel, end=" ")
