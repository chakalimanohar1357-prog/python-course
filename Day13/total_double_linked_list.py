class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):  
        self.head = None
    def Traversal(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end="<-> ")
                temp = temp.next
        print()
    def revTraversal(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            while temp:
                print(temp.data,end="<-> ")
                temp=temp.prev       
        print()
    def insertatbegin(self,data):
        new=Node(data)
        new.next=self.head
        self.head.prev=new
        self.head=new
    def insertatend(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp
    def insertatpos(self,data,pos):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next.prev=new
        new.next=temp.next
        new.prev=temp
        temp.next=new
    def delatbegin(self):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delatpos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.prev.next=temp.next
        if temp.next:
            temp.next.prev=temp.prev
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
dll=DLL()
dll.head = n1
n1.next = n2
n2.prev=n1
n2.next = n3
n3.prev=n2
n3.next = n4
n4.prev=n3
n4.next=n5
n5.prev=n4
dll.Traversal()
dll.revTraversal()
dll.insertatbegin(5)
dll.Traversal()
dll.revTraversal()
dll.insertatend(60)
dll.Traversal()
dll.revTraversal()
dll.insertatpos(25,3)
dll.Traversal()
dll.revTraversal()
dll.delatbegin()
dll.Traversal()
dll.revTraversal()
dll.delatend()
dll.Traversal()
dll.revTraversal()
dll.delatpos(3)
dll.Traversal()
dll.revTraversal()