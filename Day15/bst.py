############### bst searching element ############
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# root = Node(50)
# root.left = Node(30)
# root.right = Node(70)
# root.left.left = Node(10)
# root.left.right = Node(20)
# root.right.left = Node(60)
# root.right.right = Node(80)

# def search(root, key):
#     if root is None:
#         return False

#     if root.data == key:
#         return True

#     elif key < root.data:
#         return search(root.left, key)

#     else:
#         return search(root.right, key)
# key = 50

# if search(root, key):
#     print("Element Found")
# else:
#     print("Element Not Found")


################ insertion #####################

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# root = Node(50)
# root.left = Node(30)
# root.right = Node(70)
# root.left.left = Node(10)
# root.left.right = Node(20)
# root.right.left = Node(60)
# root.right.right = Node(80)

# # Insert a node
# def insert(root, key):
#     if root is None:
#         return Node(key)

#     if key < root.data:
#         root.left = insert(root.left, key)
#     else:
#         root.right = insert(root.right, key)

#     return root

# key = 40
# root = insert(root, key)

# print("Node Inserted")

################ deletion ###################

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Delete a node from BST

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Node with only one child or no child
        
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with two children
        
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

# Create BST

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Delete node

key = 30
root = delete(root, key)
print("Node Deleted")