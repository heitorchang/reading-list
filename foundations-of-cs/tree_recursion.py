from importlib import reload
import treeleftmost
import treebinary
# reload(treeleftmost)  # after modifying treeleftmost, then press Ctrl-Enter

from treeleftmost import TreeLeftmost
from treebinary import BinaryTree, preorder_binary_tree, inorder_binary_tree, postorder_binary_tree

# TreeLeftmost(label, leftmostChild, rightSibling)

# p. 239-240 
node_c = TreeLeftmost("c", None, None)
node_b = TreeLeftmost("b", None, node_c)
node_d = TreeLeftmost("d", None, None)
node_minus = TreeLeftmost("-", node_b, node_d)
node_times = TreeLeftmost("*", node_minus, None)
node_a = TreeLeftmost("a", None, node_times)
node_plus = TreeLeftmost("+", node_a, None)

node_plus.preorder()

node_plus.postorder()

# tree in tree_traversal.txt

node_3 = TreeLeftmost("3", None, None)
node_1 = TreeLeftmost("1", None, node_3)
node_7 = TreeLeftmost("7", None, None)
node_5 = TreeLeftmost("5", None, node_7)
node_6 = TreeLeftmost("6", node_5, None)
node_2 = TreeLeftmost("2", node_1, node_6)
node_4 = TreeLeftmost("4", node_2, None)

node_4.preorder()

node_4.postorder()

# Binary trees

# p. 256 Example 5.21

binary_node_plus = BinaryTree("+",
                              BinaryTree("a", None, None),
                              BinaryTree("*", BinaryTree("-", BinaryTree("b", None, None), BinaryTree("c", None, None)),
                                         BinaryTree("d", None, None)))

preorder_binary_tree(binary_node_plus)

inorder_binary_tree(binary_node_plus)

postorder_binary_tree(binary_node_plus)
