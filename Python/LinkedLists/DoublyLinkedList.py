class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
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
            newTail = popped.prev
            newTail.next = None
            self.tail.prev = None
            self.tail = newTail
        self.length -= 1
        return popped.val

    def unshift(self, val):
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            oldHead = self.head
            oldHead.prev = node
            node.next = oldHead
            self.head = node
        self.length += 1
        return self

    def shift(self):
        if self.length == 0:
            return None
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            newHead = self.head.next
            newHead.prev = None
            self.head.next = None
            self.head = newHead
        self.length -= 1
        return popped.val

    def getNode(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        else:
            current = self.head
            cnt = 1
            while cnt <= idx:
                current = current.next
                cnt += 1
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
        if idx == 0:
            node = self.unshift(val)
            if node: return True
        elif idx == self.length:
            node = self.push(val)
            if node: return True
        else:
            node = Node(val)
            preNode = self.getNode(idx-1)
            current = preNode.next
            preNode.next = node
            node.prev = preNode
            node.next = current
            current.prev = node
            self.length += 1
            return True
        return False

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        if idx == 0:
            return self.shift()
        elif idx == self.length - 1:
            return self.pop()
        else:
            current = self.getNode(idx)
            preNode = current.prev
            postNode = current.next
            preNode.next = postNode
            postNode.prev = preNode
            current.next = None
            current.prev = None
            self.length -= 1
            return current.val

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return self
        else:
            current = self.head
            self.head = self.tail
            self.tail = current
            while current:
                next = current.next
                current.next = current.prev
                current.prev = next
                current = next
            return self

    def print(self):
        output = []
        current = self.head
        if self.length == 0:
            return output
        while current:
            output.append(current.val)
            current = current.next
        return output

dll = DoublyLinkedList()
print(dll.getNode(0))
print(dll.unshift(1))
print(dll.print())
print(dll.unshift(2))
print(dll.print())
print(dll.unshift(3))
print(dll.print())
print(dll.unshift(4))
print(dll.print())
dll.setNode(3,100)
print(dll.print())
dll.insert(3,87)
print(dll.print())
dll.insert(2,99)
print(dll.print())
print(dll.reverse())
print(dll.print())
dll.remove(2)
print(dll.print())
dll.remove(0)
print(dll.print())
dll.remove(3)
print(dll.print())
print(dll.reverse())
print(dll.print())
