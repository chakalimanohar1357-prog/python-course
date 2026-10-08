# EXTRA (added): Queue (FIFO - first in, first out)
from collections import deque

############# queue using a list (simple, but pop(0) is slow) #############
queue = []
queue.append(10)           # enqueue
queue.append(20)
queue.append(30)
print(queue)               # [10, 20, 30]
print(queue.pop(0))        # 10 (dequeue)
print(queue[0])            # 20 (front)


############# queue using deque (recommended) #############
q = deque()
q.append(1)                # enqueue
q.append(2)
q.append(3)
print(q.popleft())         # 1 (dequeue)
print(q)                   # deque([2, 3])


############# queue class (list based) #############
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        return self.items.popleft()

    def front(self):
        return None if self.is_empty() else self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(list(self.items))


qu = Queue()
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.display()               # [5, 6, 7]
print(qu.dequeue())        # 5
print(qu.front())          # 6
print(qu.size())           # 2


############# queue using a linked list #############
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if self.rear is None:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue underflow")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


lq = LLQueue()
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.display()               # 10 -> 20 -> 30 -> None
print(lq.dequeue())        # 10
lq.display()               # 20 -> 30 -> None


############# circular queue (fixed size) #############
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.front = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            print("Queue is full")
            return
        rear = (self.front + self.count) % self.size
        self.data[rear] = value
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Queue is empty")
            return None
        value = self.data[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value


cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)              # Queue is full
print(cq.dequeue())        # 1
cq.enqueue(4)              # wraps around
print(cq.dequeue(), cq.dequeue(), cq.dequeue())   # 2 3 4


############# queue using two stacks #############
class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return None
        return self.s2.pop()


qs = QueueUsingStacks()
qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
print(qs.dequeue())        # 1
print(qs.dequeue())        # 2


############# reverse a queue using a stack #############
def reverse_queue(q):
    st = []
    while q:
        st.append(q.popleft())
    while st:
        q.append(st.pop())

rq = deque([1, 2, 3, 4])
reverse_queue(rq)
print(list(rq))            # [4, 3, 2, 1]


############# first non-repeating character in a stream #############
def first_non_repeating(stream):
    q = deque()
    count = {}
    result = []
    for ch in stream:
        count[ch] = count.get(ch, 0) + 1
        q.append(ch)
        while q and count[q[0]] > 1:
            q.popleft()
        result.append(q[0] if q else "#")
    return result

print(first_non_repeating("aabc"))     # ['a', '#', 'b', 'b']


############# deque (double ended queue) #############
dq = deque()
dq.append(2)               # add at rear
dq.appendleft(1)           # add at front
dq.append(3)
print(dq)                  # deque([1, 2, 3])
print(dq.pop())            # 3 (remove from rear)
print(dq.popleft())        # 1 (remove from front)
dq.extend([7, 8])
dq.rotate(1)               # rotate right by 1
print(dq)                  # deque([8, 2, 7])


############# priority queue (smallest value comes out first) #############
import heapq

pq = []
heapq.heappush(pq, 30)
heapq.heappush(pq, 10)
heapq.heappush(pq, 20)
print(heapq.heappop(pq))   # 10
print(pq[0])               # 20 (peek)

# with priorities: (priority, task) - lower number = higher priority
tasks = []
heapq.heappush(tasks, (2, "write code"))
heapq.heappush(tasks, (1, "fix bug"))
heapq.heappush(tasks, (3, "relax"))
while tasks:
    print(heapq.heappop(tasks)[1])     # fix bug, write code, relax

# max priority queue: store negative values
mx = []
for n in [4, 9, 2]:
    heapq.heappush(mx, -n)
print(-heapq.heappop(mx))  # 9


############# queue module (ready made, thread safe) #############
from queue import Queue, LifoQueue

rq1 = Queue()
rq1.put(1)
rq1.put(2)
print(rq1.get())           # 1 (FIFO)
print(rq1.qsize())         # 1
print(rq1.empty())         # False

lifo = LifoQueue()         # works like a stack
lifo.put(1)
lifo.put(2)
print(lifo.get())          # 2 (LIFO)


############# generate binary numbers from 1 to n #############
def generate_binary(n):
    q = deque(["1"])
    result = []
    for _ in range(n):
        cur = q.popleft()
        result.append(cur)
        q.append(cur + "0")
        q.append(cur + "1")
    return result

print(generate_binary(5))  # ['1', '10', '11', '100', '101']


############# hot potato / josephus (circle elimination) #############
def hot_potato(names, k):
    q = deque(names)
    while len(q) > 1:
        q.rotate(-(k - 1))     # pass the potato k-1 times
        q.popleft()            # k-th person is out
    return q[0]

print(hot_potato(["A", "B", "C", "D", "E"], 3))   # D


############# sliding window maximum (monotonic deque) #############
def sliding_window_max(arr, k):
    dq = deque()                   # stores indexes, values decreasing
    result = []
    for i in range(len(arr)):
        if dq and dq[0] <= i - k:  # out of window
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]


############# queue in action: BFS on a graph (see Day16) #############
def bfs(graph, start):
    visited = [start]
    q = deque([start])
    while q:
        node = q.popleft()
        for nb in graph[node]:
            if nb not in visited:
                visited.append(nb)
                q.append(nb)
    return visited

g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
print(bfs(g, 'A'))         # ['A', 'B', 'C', 'D']
