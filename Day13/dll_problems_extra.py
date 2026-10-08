# EXTRA (added): doubly linked list problems (reverse, search, count)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def build(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head


def show(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")


################ reverse a doubly linked list ################
def reverse(head):
    temp = head
    new_head = head
    while temp:
        temp.prev, temp.next = temp.next, temp.prev   # swap links
        new_head = temp
        temp = temp.prev                              # old next
    return new_head


head = build([10, 20, 30, 40])
show(head)                 # 10 <-> 20 <-> 30 <-> 40 <-> None
head = reverse(head)
show(head)                 # 40 <-> 30 <-> 20 <-> 10 <-> None


################ search an element ################
def search(head, key):
    temp = head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False


print("Search 30:", search(head, 30))   # True
print("Search 99:", search(head, 99))   # False


################ count nodes ################
def count(head):
    c = 0
    temp = head
    while temp:
        c += 1
        temp = temp.next
    return c


print("Count:", count(head))            # 4
