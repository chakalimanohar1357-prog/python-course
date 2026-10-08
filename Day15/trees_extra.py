# EXTRA (added): common binary tree / BST problems that were missing
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)


############# level order traversal (BFS) #############
def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("Level order:")
level_order(root)          # 10 20 30 40 50
print()


############# height of tree #############
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

print("Height:", height(root))          # 3


############# count of nodes #############
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

print("Nodes:", count_nodes(root))      # 5


############# count of leaf nodes #############
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

print("Leaves:", count_leaves(root))    # 3


############# sum of all nodes #############
def tree_sum(root):
    if root is None:
        return 0
    return root.data + tree_sum(root.left) + tree_sum(root.right)

print("Sum:", tree_sum(root))           # 150


############# maximum value in a binary tree #############
def max_value(root):
    if root is None:
        return float("-inf")
    return max(root.data, max_value(root.left), max_value(root.right))

print("Max:", max_value(root))          # 50


############# mirror (invert) a binary tree #############
def mirror(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)

mirror(root)
print("Level order after mirror:")
level_order(root)          # 10 30 20 50 40
print()
mirror(root)               # restore


############# check if a tree is a valid BST #############
def is_bst(root, low=float("-inf"), high=float("inf")):
    if root is None:
        return True
    if not (low < root.data < high):
        return False
    return is_bst(root.left, low, root.data) and is_bst(root.right, root.data, high)

print("Is BST (binary tree above):", is_bst(root))   # False

bst = Node(50)
bst.left = Node(30)
bst.right = Node(70)
bst.left.left = Node(20)
bst.left.right = Node(40)
print("Is BST (bst):", is_bst(bst))                  # True
