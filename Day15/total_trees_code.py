class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def delete1(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
    return root
def delete_one_child(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete_one_child(root.left, key)
    elif key > root.data:
        root.right = delete_one_child(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
    return root
def delete(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root
def minvalue(root):
    temp=root
    while temp.left:
        temp=temp.left
    return temp.data
root = Node(50)
root.left = Node(30)
root.right = Node(80)
root.left.left = Node(10)
root.left.right = Node(40)
root.right.left = Node(70)
#root.right.right = Node(90)
print(search(root, 70))
insert(root, 100)
inorder(root)
print("\n")
delete1(root,100)
inorder(root)
print("\n")
delete_one_child(root,80)
inorder(root)
print("\n")
delete(root,50)
inorder(root)
print("\n")
print(minvalue(root))