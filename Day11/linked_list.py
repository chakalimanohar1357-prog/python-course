#############linked list ############

# class Node:
#     def __init__ (self,data):
#         self.data = data
#         self.next = None
# class SLL:
#     def __init__(self):
#         self.head = None
#     def Traversal(self):
#         if self.head is Node:
#             print("linked list is empty")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data,end="-> ")
#                 temp = temp.next
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n5=Node(50)
# sll= SLL()
# sll.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# sll.Traversal()
# temp = n1
# while temp:
#     print(temp.data)
#     temp = temp.next


########### insertion of node at begin ##############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# # Take new node from user
# num = int(input("Enter new node value: "))
# new_node = Node(num)

# # Insert at beginning
# new_node.next = node1
# node1 = new_node

# # Display linked list
# temp = node1
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")




##############adding last#############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# # Add node at the end
# num = int(input("Enter new node value: "))
# new_node = Node(num)

# temp = node1
# while temp.next:
#     temp = temp.next

# temp.next = new_node

# # Display linked list
# temp = node1
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")

##############adding node at middle #################3

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# # Take new node value and position
# num = int(input("Enter new node value: "))
# pos = int(input("Enter position: "))

# new_node = Node(num)

# # Insert at beginning
# if pos == 1:
#     new_node.next = node1
#     node1 = new_node
# else:
#     temp = node1
#     for i in range(pos - 2):
#         temp = temp.next

#     new_node.next = temp.next
#     temp.next = new_node

# # Display linked list
# temp = node1
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next

# print("None")



################### deletion at start of linked list###########
#Delete First Node 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# head = node1

# # Delete first node
# temp = head
# head = head.next
# temp = None

# # Display linked list
# temp = head
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# print("None")

############################## delete node at last ###############
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Delete last node
temp = node1

while temp.next.next:
    temp = temp.next

temp.next = None

# Display linked list
temp = node1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")