class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Connect nodes
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

node4.next = node5
node5.prev = node4

head = node1

# Forward Traversal
print("Forward Traversal:")
temp = head
while temp:
    print(temp.data, end=" <-> ")
    last = temp      # Store last node
    temp = temp.next
print("None")

# Backward Traversal
print("Backward Traversal:")
temp = last
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.prev
print("None")