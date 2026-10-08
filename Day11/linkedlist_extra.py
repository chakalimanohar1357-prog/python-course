# EXTRA (added): linked list problems that were missing from linkedlist_problems.py
# (your cycle detection section was only a stub).

class Node:
    def __init__(self, data):
        self.data = data
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
            tail = node
    return head


def show(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


#################### linked list cycle detection (Floyd's slow/fast) ###############
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


head = build([1, 2, 3, 4, 5])
print("Cycle:", has_cycle(head))            # False
head.next.next.next.next.next = head.next    # 5 points back to 2 -> cycle
print("Cycle:", has_cycle(head))            # True


#################### reverse a linked list ###############
def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


head = build([1, 2, 3, 4, 5])
show(head)                # 1 -> 2 -> 3 -> 4 -> 5 -> None
head = reverse(head)
show(head)                # 5 -> 4 -> 3 -> 2 -> 1 -> None


#################### middle of a linked list ###############
def middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data


print("Middle:", middle(build([1, 2, 3, 4, 5])))      # 3
print("Middle:", middle(build([1, 2, 3, 4, 5, 6])))   # 4 (second middle)
