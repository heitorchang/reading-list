class BstNode:
    # p. 286, 287
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def inorder_tree_walk(self):
        if self.left:
            self.left.inorder_tree_walk()
        print(self.key)
        if self.right:
            self.right.inorder_tree_walk()

    def add_left(self, left):
        left.parent = self
        self.left = left

    def add_right(self, right):
        right.parent = self
        self.right = right

    # p. 290
    def tree_search(self, key):
        node = self
        if not node or node.key == key:
            return node
        if key < node.key and self.left:
            return self.left.tree_search(key)
        elif self.right:
            return self.right.tree_search(key)

    def tree_search_iterative(self, key):
        node = self
        while node and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node
        
    def __repr__(self):
        return "BstNode[{}]".format(self.key)

    # p. 291
    def tree_minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def tree_maximum(self):
        node = self
        while node.right:
            node = node.right
        return node

# using functions instead of methods from here onward

def tree_minimum(node):
    while node.left:
        node = node.left
    return node
    
def tree_maximum(node):
    while node.right:
        node = node.right
    return node
        
def tree_successor(x):
    # p. 292
    if x.right:
        return tree_minimum(x.right)
    y = x.parent
    while y and x == y.right:
        x = y
        y = y.parent
    return y

def tree_predecessor(x):
    # ex. 12.2-3
    if x.left:
        return tree_maximum(x.left)
    y = x.parent
    while y and x == y.left:
        x = y
        y = y.parent
    return y


def tree_insert(T, z):
    # p. 294
    y = None
    x = T  # T.root
    while x:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if not y:
        T = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):
    # p. 296
    if not u.parent:
        T = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v:
        v.parent = u.parent

def tree_delete(T, z):
    if not z.left:
        transplant(T, z, z.right)
    elif not z.right:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.parent != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y
    
    
def test():
    #    9
    #   / \
    #  2   12
    #     /
    #    10
    b = BstNode(9)
    left = BstNode(2)
    right = BstNode(12)
    right_left = BstNode(10)
    b.add_left(left)
    b.add_right(right)
    right.add_left(right_left)

    b.inorder_tree_walk()

    print(b.tree_search(10))
    print(b.tree_search(99))
    print(b.tree_search_iterative(10))
    print(b.tree_search_iterative(99))

    print(b.tree_minimum())
    print(b.tree_maximum())

    testeql(tree_successor(b).key, 10)
    testeql(tree_successor(right), None)
    testeql(tree_successor(right_left).key, 12)
    testeql(tree_successor(left).key, 9)

    testeql(tree_predecessor(b).key, 2)
    testeql(tree_predecessor(left), None)
    testeql(tree_predecessor(right).key, 10)
    testeql(tree_predecessor(right_left).key, 9)

    tree_insert(b, BstNode(3))
    tree_insert(b, BstNode(11))
    b.inorder_tree_walk()

    tree_delete(b, right_left)
    b.inorder_tree_walk()
