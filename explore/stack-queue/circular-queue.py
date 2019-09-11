class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [None] * k
        self.tail = 0
        self.size = 0
        self.cap = k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail+1) % self.cap
        self.size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.tail-self.size+self.cap) % self.cap]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.tail-1+self.cap) % self.cap]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.cap


def main():
    k = 3
    q = MyCircularQueue(k)
    assert(q.enQueue(1))
    assert(q.enQueue(2))
    assert(q.enQueue(3))
    assert(q.enQueue(4) == False)
    assert(q.Rear() == 3)
    assert(q.isFull())
    assert(q.deQueue() != -1)
    assert(q.enQueue(4))
    assert(q.Rear() == 4)


if __name__ == '__main__':
    main()
