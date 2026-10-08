######33333sum of elements in linked list ###########

# class Node:
#     sum = 0
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n5=Node(50)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# head = n1
# temp = head
# sum = 0
# while temp:
#     print(temp.data,end="->")
#     sum += temp.data
#     temp=temp.next
# print("none")
# print(sum)
 
 
 ################count of no of nodes in ll##########
 
# class Node:
#     sum = 0
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n5=Node(50)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# head = n1
# temp = head
# count = 0
# while temp:
#     print(temp.data,end="->")
#     count += 1
#     temp=temp.next
# print("none")
# print(count)

################ sum of even elements i ll #######

# class Node:
#     sum = 0
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# n1=Node(7)
# n2=Node(20)
# n3=Node(35)
# n4=Node(40)
# n5=Node(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# head = n1
# temp = head
# sum = 0
# while temp:
#     print(temp.data,end="->")
#     if (temp.data)%2==0:
#         sum += 1
#     temp=temp.next
# print("none")
# print(sum)

################################# sum of node in ll #############

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# n1 = Node(7)
# n2 = Node(20)
# n3 = Node(35)
# n4 = Node(40)
# n5 = Node(5)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = n1
# temp = head

# sum = 0
# pos = 1

# while temp:
#     print(temp.data, end="->")

#     if pos % 2 == 0:
#         sum += temp.data

#     pos += 1 
#     temp = temp.next

# print("None")
# print("Sum of even position elements =", sum)


################## search if element present in it or not###########

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# n1 = Node(7)
# n2 = Node(20)
# n3 = Node(35)
# n4 = Node(40)
# n5 = Node(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# head = n1
# temp = head
# val = 35
# while temp:
#     if temp.data == val:
#         print("Found")
#         break
#     temp = temp.next
# else:
#     print("Not Found")


############### find min,max elements in ll ###################

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Create nodes
# n1 = Node(7)
# n2 = Node(20)
# n3 = Node(35)
# n4 = Node(40)
# n5 = Node(5)

# # Link nodes
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = n1

# # Initialize max and min with the first node
# maximum  = head.data
# minimum = head.data
# temp = head

# while temp:
#     print(temp.data, end="->")

#     if temp.data > maximum:
#         maximum = temp.data

#     if temp.data < minimum:
#         minimum = temp.data

#     temp = temp.next

# print("None")
# print(maximum)
# print(minimum)

################################ nth element from begining ####################3

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Create nodes
# n1 = Node(7)
# n2 = Node(20)
# n3 = Node(35)
# n4 = Node(40)
# n5 = Node(5)

# # Link nodes
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = n1

# # Find nth element
# n = 3
# temp = head
# count = 1

# while temp:
#     if count == n:
#         print(f"{n}rd element from beginning =", temp.data)
#         break
#     temp = temp.next
#     count += 1
# else:
#     print("Position out of range")
    
######################### nth element from end #################

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Create nodes
# n1 = Node(7)
# n2 = Node(20)
# n3 = Node(35)
# n4 = Node(40)
# n5 = Node(5)

# # Link nodes
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = n1

# # Count total nodes
# count = 0
# temp = head
# while temp:
#     count += 1
#     temp = temp.next

# n = 3

# if n > count or n <= 0:
#     print("Invalid Position")
# else:
#     pos = count - n

#     temp = head
#     for i in range(pos):
#         temp = temp.next

#     print(f"{n}th element from end =", temp.data)


#################### linked list cycle detection #################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


        

        