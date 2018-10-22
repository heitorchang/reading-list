import os

os.chdir("c:\\Users\\Heitor\\Desktop\\emacs-24.3\\bin\\reading-list\\interactive-py\\trees\\")

from binarytree import BinaryTree

def test():
    bt = BinaryTree(1)
    bt.insertLeft(2)
    bt.insertLeft(3)

    assert bt.left.key == 3
    assert bt.left.left.key == 2
    print("assertions ok")
