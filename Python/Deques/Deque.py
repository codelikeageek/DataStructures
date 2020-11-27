class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addFront(self,val):
        newNode = Node(val)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.first.prev = newNode
            newNode.next = self.first
            self.first = newNode
        self.size += 1
        return self

    def addRear(self,val):
        newNode = Node(val)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            newNode.prev = self.last
            self.last = newNode
        self.size += 1
        return self

    def removeFront(self):
        if self.size == 0:
            return None
        popped = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            newHead = popped.next
            newHead.prev = None
            popped.next = None
            self.first = newHead
        self.size -= 1
        return popped.val

    def removeRear(self):
        if self.size == 0:
            return None
        popped = self.last
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            newTail = popped.prev
            newTail.next = None
            popped.prev = None
            self.last = newTail
        self.size -= 1
        return popped.val

    def getSize(self):
        return self.size

    def printDeque(self):
        output = []
        size = self.size
        current = self.first
        while size > 0:
            output.append(current.val)
            current = current.next
            size -= 1
        return output

deque = Deque()
deque.addFront(5)
print(deque.printDeque())
deque.addFront(6)
print(deque.printDeque())
print(deque.printDeque())
deque.addRear(17)
print(deque.printDeque())
deque.addRear(18)
print(deque.printDeque())
print(deque.getSize())
print(deque.removeFront())
print(deque.printDeque())
print(deque.removeRear())
print(deque.printDeque())