class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, val):
        newNode = Node(val)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            return None
        currentHead = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            newHead = currentHead.next
            currentHead.next = None
            self.first = newHead
        self.size -= 1
        return currentHead.val

    def getNode(self,idx):
        if idx < 0 or idx >= self.size:
            return None
        current = self.first
        cnt = 1
        while cnt <= idx:
            current = current.next
            cnt += 1
        return current.val

    def getSize(self):
        return self.size

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.getSize())
print(queue.getNode(0))
print(queue.getNode(1))
print(queue.getNode(2))
print(queue.getNode(3))
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())