#!/usr/bin/env python3

"""
https://leetcode.cn/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""


class Node:
    def __init__(self, v: int):
        self.v: int = v
        self.pre: Node | None = None
        self.next: Node | None = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.head = None

    def print(self):
        print("values: ", end=":")
        if self.head is None:
            assert self.size == 0
            print("none")

        n = self.head
        output = []
        while True:
            output.append(str(n.v))
            n = n.next
            if n is self.head:
                break
        print(" ".join(output))

    def insertFront(self, value: int) -> bool:
        if self.cap <= self.size:
            return False
        node = Node(value)
        if self.head is None:
            self.head = node
            node.pre = node
            node.next = node
        else:
            tail = self.head.pre

            node.next = self.head
            node.pre = tail
            tail.next = node
            self.head.pre = node

            self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.cap <= self.size:
            return False
        node = Node(value)
        if self.head is None:
            self.head = node
            node.pre = node
            node.next = node
        else:
            tail = self.head.pre

            node.pre = tail
            node.next = self.head
            tail.next = node
            self.head.pre = node

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.head is None:
            return False

        if self.head.pre is self.head:
            self.head = None
        else:
            tail = self.head.pre
            self.head = self.head.next
            tail.next = self.head
            self.head.pre = tail

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.head is None:
            return False
        if self.head.pre is self.head:
            self.head = None
        else:
            tail = self.head.pre
            self.head.pre = tail.pre
            tail.pre.next = self.head

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.v

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.pre.v

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


obj = MyCircularDeque(3)

print("insert 8")
r = obj.insertFront(8)
print(r)
obj.print()

print("insert 8")
r = obj.insertLast(8)
print(r)
obj.print()

print("insert 2")
r = obj.insertLast(2)
print(r)
obj.print()

print("get front")
r = obj.getFront()
print(r)
obj.print()

print("delete last")
r = obj.deleteLast()
print(r)
obj.print()

print("get rear")
r = obj.getRear()
print(r)
obj.print()

print("insert 9")
r = obj.insertFront(9)
print(r)
obj.print()

print("delte front")
r = obj.deleteFront()
print(r)
obj.print()

print("get rear")
r = obj.getRear()
print(r)
obj.print()

print("insert last 2")
r = obj.insertLast(2)
print(r)
obj.print()

print("is full")
r = obj.isFull()
print(r)
obj.print()
