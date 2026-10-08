# EXTRA (added): Stack (LIFO - last in, first out)

############# stack using a list #############
stack = []
stack.append(10)           # push
stack.append(20)
stack.append(30)
print(stack)               # [10, 20, 30]
print(stack.pop())         # 30  (pop)
print(stack[-1])           # 20  (peek)
print(len(stack) == 0)     # False (is empty?)


############# stack class (list based) #############
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()                # [1, 2, 3]
print(s.pop())             # 3
print(s.peek())            # 2
print(s.size())            # 2


############# stack using a linked list #############
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LLStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print("Stack underflow")
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return None if self.top is None else self.top.data

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ls = LLStack()
ls.push(10)
ls.push(20)
ls.push(30)
ls.display()               # 30 -> 20 -> 10 -> None
print(ls.pop())            # 30
print(ls.peek())           # 20


############# reverse a string using stack #############
def reverse_string(text):
    st = []
    for ch in text:
        st.append(ch)
    result = ""
    while st:
        result += st.pop()
    return result

print(reverse_string("python"))   # nohtyp


############# balanced parentheses #############
def is_balanced(expr):
    st = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in expr:
        if ch in "([{":
            st.append(ch)
        elif ch in ")]}":
            if not st or st.pop() != pairs[ch]:
                return False
    return len(st) == 0

print(is_balanced("{[()]}"))      # True
print(is_balanced("{[(])}"))      # False
print(is_balanced("(("))          # False


############# postfix expression evaluation #############
def eval_postfix(expr):
    st = []
    for token in expr.split():
        if token.lstrip("-").isdigit():
            st.append(int(token))
        else:
            b = st.pop()
            a = st.pop()
            if token == "+":
                st.append(a + b)
            elif token == "-":
                st.append(a - b)
            elif token == "*":
                st.append(a * b)
            elif token == "/":
                st.append(a // b)
    return st.pop()

print(eval_postfix("2 3 1 * + 9 -"))   # -4


############# next greater element #############
def next_greater(arr):
    result = [-1] * len(arr)
    st = []                       # stores indexes
    for i in range(len(arr)):
        while st and arr[i] > arr[st[-1]]:
            result[st.pop()] = arr[i]
        st.append(i)
    return result

print(next_greater([4, 5, 2, 25]))     # [5, 25, 25, -1]


############# stack using deque (faster than list at both ends) #############
from collections import deque

dst = deque()
dst.append(1)              # push
dst.append(2)
dst.append(3)
print(dst.pop())           # 3 (pop)
print(dst[-1])             # 2 (peek)


############# min stack (get the minimum in O(1)) #############
class MinStack:
    def __init__(self):
        self.items = []
        self.mins = []                 # mins[-1] is always the current minimum

    def push(self, data):
        self.items.append(data)
        if not self.mins or data <= self.mins[-1]:
            self.mins.append(data)

    def pop(self):
        if not self.items:
            print("Stack underflow")
            return None
        data = self.items.pop()
        if data == self.mins[-1]:
            self.mins.pop()
        return data

    def get_min(self):
        return None if not self.mins else self.mins[-1]


ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(3)
print(ms.get_min())        # 3
ms.pop()
ms.pop()
print(ms.get_min())        # 3
ms.pop()
print(ms.get_min())        # 5


############# stack using two queues #############
class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        self.q2.append(data)
        while self.q1:                 # move old items behind the new one
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def peek(self):
        return self.q1[0] if self.q1 else None


sq = StackUsingQueues()
sq.push(1)
sq.push(2)
sq.push(3)
print(sq.pop())            # 3
print(sq.peek())           # 2


############# sort a stack (using recursion) #############
def insert_sorted(st, value):
    if not st or st[-1] <= value:
        st.append(value)
        return
    top = st.pop()
    insert_sorted(st, value)
    st.append(top)

def sort_stack(st):
    if not st:
        return
    top = st.pop()
    sort_stack(st)
    insert_sorted(st, top)

data = [30, -5, 18, 14, -3]
sort_stack(data)
print(data)                # [-5, -3, 14, 18, 30]  (top is the largest)


############# infix to postfix #############
def infix_to_postfix(expr):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    st = []
    result = []
    for ch in expr:
        if ch.isalnum():
            result.append(ch)
        elif ch == '(':
            st.append(ch)
        elif ch == ')':
            while st and st[-1] != '(':
                result.append(st.pop())
            st.pop()                   # remove '('
        else:
            while st and st[-1] != '(' and prec[st[-1]] >= prec[ch]:
                result.append(st.pop())
            st.append(ch)
    while st:
        result.append(st.pop())
    return "".join(result)

print(infix_to_postfix("a+b*c"))        # abc*+
print(infix_to_postfix("(a+b)*c"))      # ab+c*


############# remove adjacent duplicates #############
def remove_adjacent_duplicates(text):
    st = []
    for ch in text:
        if st and st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
    return "".join(st)

print(remove_adjacent_duplicates("abbaca"))    # ca


############# daily temperatures (days until a warmer day) #############
def daily_temperatures(temps):
    result = [0] * len(temps)
    st = []                       # stores indexes
    for i in range(len(temps)):
        while st and temps[i] > temps[st[-1]]:
            j = st.pop()
            result[j] = i - j
        st.append(i)
    return result

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]


############# stack and recursion #############
# Every recursive call is pushed on the "call stack" and popped when it returns.
# That is why very deep recursion gives RecursionError (stack overflow).
def countdown(n):
    if n == 0:
        return
    print(n, end=" ")
    countdown(n - 1)

countdown(3)               # 3 2 1
print()
