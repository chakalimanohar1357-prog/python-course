class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):  
        self.head = None
    def Traversal(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="-> ")
                temp = temp.next
        print()
    
    def insertatbegin(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def insertatend(self,data):
        new=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new
    def insertatpos(self,data,pos):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new
    def delatbegin(self):
        self.head=self.head.next
    def delatend(self):
        temp=self.head
        prev=None
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
    def delatend2(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def delatpos(self,pos):
        temp=self.head
        prev=None
        for i in range(pos-1):
            prev=temp
            temp=temp.next
        prev.next=temp.next
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
sll = SLL()
sll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next=n5
sll.Traversal()
sll.insertatbegin(5)
sll.Traversal()
sll.insertatend(60)
sll.Traversal()
sll.insertatpos(25,3)
sll.Traversal()
sll.delatbegin()
sll.Traversal()
sll.delatend()
sll.Traversal()
sll.delatend2()
sll.Traversal()
sll.delatpos(3)
sll.Traversal()