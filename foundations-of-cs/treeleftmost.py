# p. 240 Tree (Leftmost-child--right-sibling representation)

class TreeLeftmost:
    def __init__(self, nodeLabel, leftmostChild, rightSibling):
        self.nodeLabel = nodeLabel
        self.leftmostChild = leftmostChild
        self.rightSibling = rightSibling

    def __str__(self):
        return "TreeLeftmost : root(%s)" % (self.nodeLabel)

    def preorder(self):
        print("Preorder traversal: ", end="")
        self.preorder_traverse()
        print()
        
    def preorder_traverse(self):
        print("%s" % (self.nodeLabel), end=" ")
        child = self.leftmostChild
        while child is not None:
            child.preorder_traverse()
            child = child.rightSibling

    def postorder(self):
        print("Postoder traversal: ", end="")
        self.postorder_traverse()
        print()

    def postorder_traverse(self):
        child = self.leftmostChild
        while child is not None:
            child.postorder_traverse()
            child = child.rightSibling
        print("%s" % (self.nodeLabel), end=" ")
