class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self,val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            previous = current
            while current.next:
                previous = current
                current = current.next
            self.tail = previous
            self.tail.next = None
        self.length -= 1
        return popped.val

    def shift(self):
        if self.length == 0:
            return None
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = oldHead.next
            oldHead.next = None
        self.length -= 1
        return oldHead.val

    def unshift(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self

    def getNode(self, idx):
        if self.length == 0 or idx < 0 or idx >= self.length:
            return None
        elif idx == 0:
            return self.head
        elif idx == self.length - 1:
            return self.tail
        else:
            current = self.head
            cnt = 1
            while cnt <= idx:
                cnt += 1
                current = current.next
            return current

    def setNode(self, idx, val):
        node = self.getNode(idx)
        if node:
            node.val = val
            return True
        else:
            return False

    def insert(self, idx, val):
        if idx < 0 or idx > self.length:
            return False
        elif idx == 0:
            newNode = self.unshift(val)
            if newNode: return True
        elif idx == self.length:
            newNode = self.push(val)
            if newNode: return True
        else:
            node = Node(val)
            current = self.getNode(idx)
            previous = self.getNode(idx-1)
            previous.next = node
            node.next = current
            self.length += 1
            return True

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None;
        if idx == 0:
            return self.shift()
        elif idx == self.length - 1:
            return self.pop()
        else:
            previous = self.getNode(idx-1)
            current = previous.next
            previous.next = current.next
            current.next = None
            self.length -= 1
            return current.val

    def print(self):
        output = []
        if self.length == 0:
            return output
        else:
            current = self.head
            while current:
                output.append(current.val)
                current = current.next
        return output

    def reverse(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self
        else:
            current = self.head
            self.head = self.tail
            self.tail = self.head
            prev = None
            next = None
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return self

