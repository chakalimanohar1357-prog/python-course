######## tree creation ###############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50)
# print(root.data)
# print(root.left.data)
# print(root.right.data)
# print(root.left.left.data)
# print(root.left.right.data)

#################### pre,in,post orders ####################3
######## Tree Creation ########
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

######## Preorder ########
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

######## Inorder ########
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

######## Postorder ########
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)
