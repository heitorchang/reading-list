class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        newTree = BinaryTree(newNode)
        if self.left:
            newTree.left = self.left
        self.left = newTree

    def insertRight(self, newNode):
        newTree = BinaryTree(newNode)
        if self.right:
            newTree.right = self.right
        self.right = newTree

        
