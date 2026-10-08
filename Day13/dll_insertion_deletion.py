################ inser at begining##############3

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2

# head = node1

# # New node
# new_node = Node(5)

# # Insert at beginning
# new_node.next = head
# head.prev = new_node
# head = new_node

# # Display
# temp = head
# while temp:
#     print(temp.data, end=" <-> ")
#     temp = temp.next
# print("None")


########### insert at end ##################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2

# head = node1

# new_node = Node(40)

# temp = head
# while temp.next:
#     temp = temp.next

# temp.next = new_node
# new_node.prev = temp

# # Display
# temp = head
# while temp:
#     print(temp.data, end=" <-> ")
#     temp = temp.next
# print("None")

################# insert at specific position #################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# # Create list: 10 <-> 20 <-> 30
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# n1.next = n2
# n2.prev = n1

# n2.next = n3
# n3.prev = n2

# head = n1

# # New node
# num = int(input("Enter value: "))
# pos = int(input("Enter position: "))
# new = Node(num)

# temp = head

# # Move to (position-1)
# for i in range(pos - 2):
#     temp = temp.next

# new.next = temp.next
# new.prev = temp

# if temp.next:
#     temp.next.prev = new

# temp.next = new

# # Display
# temp = head
# while temp:
#     print(temp.data, end=" <-> ")
#     temp = temp.next

# print("None")

############################### delete 1st node ##################

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2

# head = node1

# # Delete first node
# head = head.next
# head.prev = None

# # Display
# temp = head
# while temp:
#     print(temp.data, end=" <-> ")
#     temp = temp.next
# print("None")

###################### delete last node ###############

# class Node:
#     def __init__(self,
# data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)+

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2

# head = node1

# temp = head
# while temp.next:
#     temp = temp.next

# temp.prev.next = None

# # Display
# temp = head
# while temp:
#     print(temp.data, end=" <-> ")
#     temp = temp.next
# print("None")

########################## delete at pos ###################

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.prev = n1

n2.next = n3
n3.prev = n2

n3.next = n4
n4.prev = n3

head = n1

pos = int(input("Enter position: "))

temp = head

# Move to the position
for i in range(pos - 1):
    temp = temp.next

temp.prev.next = temp.next

if temp.next:
    temp.next.prev = temp.prev

# Display
temp = head
while temp:
    print(temp.data, end=" <-> ") 
    temp = temp.next

print("None")