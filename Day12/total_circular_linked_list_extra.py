# EXTRA (added): complete Circular Linked List class.
# Your circular_linked_list.py had "deletion at end" empty and no delete-at-position,
# so this file puts every operation in one class (same style as total_linked_list.py).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    def Traversal(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    def insertatbegin(self, data):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new.next = self.head
        temp.next = new
        self.head = new

    def insertatend(self, data):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    def insertatpos(self, data, pos):
        if pos == 1:
            self.insertatbegin(data)
            return
        new = Node(data)
        temp = self.head
        for i in range(pos - 2):
            temp = temp.next
        new.next = temp.next
        temp.next = new

    def delatbegin(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return
        if self.head.next == self.head:      # only one node
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def delatend(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return
        if self.head.next == self.head:      # only one node
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def delatpos(self, pos):
        if pos == 1:
            self.delatbegin()
            return
        temp = self.head
        for i in range(pos - 2):
            temp = temp.next
        temp.next = temp.next.next


cll = CLL()
for value in (10, 20, 30, 40):
    cll.insertatend(value)
cll.Traversal()          # 10 -> 20 -> 30 -> 40 -> (head)
cll.insertatbegin(5)
cll.Traversal()          # 5 -> 10 -> 20 -> 30 -> 40 -> (head)
cll.insertatpos(25, 4)
cll.Traversal()          # 5 -> 10 -> 20 -> 25 -> 30 -> 40 -> (head)
cll.delatbegin()
cll.Traversal()          # 10 -> 20 -> 25 -> 30 -> 40 -> (head)
cll.delatend()
cll.Traversal()          # 10 -> 20 -> 25 -> 30 -> (head)
cll.delatpos(3)
cll.Traversal()          # 10 -> 20 -> 30 -> (head)
