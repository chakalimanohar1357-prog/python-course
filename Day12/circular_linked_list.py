# ################circular linked list #################3
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n1      
# head = n1
# temp = head
# while True:
#     print(temp.data, end=" -> ")
#     temp = temp.next
#     if temp == head:
#         break

# print("head")


################ insert at begin #############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n1

# head = n1

# # Insert at beginning
# new = Node(5)

# temp = head
# while temp.next != head:
#     temp = temp.next

# new.next = head
# temp.next = new
# head = new

# # Display Circular Linked List
# temp = head
# while True:
#     print(temp.data, end=" -> ")
#     temp = temp.next
#     if temp == head:
#         break
# print("(head)")


############insert at end #############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n1

# head = n1
# new = Node(5)

# temp = head
# while temp.next != head:
#     temp = temp.next

# new.next = head
# temp.next = new
# # Display Circular Linked List
# temp = head
# while True:
#     print(temp.data, end=" -> ")
#     temp = temp.next
#     if temp == head:
#         break
# print("(head)")

###################3 insert at pos ####################

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n1

# head = n1

# new = Node(int(input("Enter value: ")))
# pos = int(input("Enter position: "))

# temp = head

# for i in range(pos - 2):
#     temp = temp.next

# new.next = temp.next
# temp.next = new

# # Display
# temp = head
# while True:
#     print(temp.data, end=" -> ")
#     temp = temp.next
#     if temp == head:
#         break
# print("(head)")

##################### deletion at begin ########################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Create Circular Linked List
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n1

# head = n1

# # Delete at beginning
# temp = head

# while temp.next != head:
#     temp = temp.next

# temp.next = head.next
# head = head.next

# # Display
# temp = head
# while True:
#     print(temp.data, end=" -> ")
#     temp = temp.next
#     if temp == head:
#         break

# print("(head)")


################# deletion at end #########################