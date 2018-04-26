import os

os.chdir("c:\\Users\\Heitor\\Desktop\\emacs-24.3\\bin\\reading-list\\interactive-py\\trees\\")


# https://runestone.academy/runestone/static/pythonds/Trees/TreeTraversals.html

from binarytree import BinaryTree
import operator

desc = """think of tree traversal as drawing a counterclockwise outline of the tree structure. Every node has a left, bottom-middle, and right point. preorder is like printing the node's key when the left point is touched, inorder the middle, and postorder the right"""

def preorder(tree):
    # this is like reading a book in order
    if tree:
        print(tree.key)
        preorder(tree.left)
        preorder(tree.right)
        
def inorder(tree):
    # prints a 'flattened' representation of the tree
    if tree:
        inorder(tree.left)
        print(tree.key)
        inorder(tree.right)

def postorder(tree):
    # parse trees
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.key)

def postordereval(tree):
    # save values of children and apply a function
    if tree:
        resLeft = postordereval(tree.left)
        resRight = postordereval(tree.right)
        if resLeft and resRight:
            return tree.key(resLeft, resRight)
        else:
            return tree.key
        
def test():
    book = BinaryTree("Book")
    ch1 = BinaryTree("Ch. 1")
    ch2 = BinaryTree("Ch. 2")
    sec11 = BinaryTree("Section 1.1")
    sec12 = BinaryTree("Section 1.2")
    sec121 = BinaryTree("Section 1.2.1")
    sec122 = BinaryTree("Section 1.2.2")
    sec21 = BinaryTree("Section 2.1")
    sec22 = BinaryTree("Section 2.2")
    sec221 = BinaryTree("Section 2.2.1")
    sec222 = BinaryTree("Section 2.2.2")

    sec12.left = sec121
    sec12.right = sec122

    sec22.left = sec221
    sec22.right = sec222

    ch1.left = sec11
    ch1.right = sec12

    ch2.left = sec21
    ch2.right = sec22

    book.left = ch1
    book.right = ch2

    
    # preorder(book)
    # postorder(book)
    inorder(book)

    equation = BinaryTree(operator.add)
    equation.left = BinaryTree(3)

    mult = BinaryTree(operator.mul)
    mult.left = BinaryTree(4)
    mult.right = BinaryTree(5)

    equation.right = mult

    # print(postordereval(equation))

    # inorder(equation)
