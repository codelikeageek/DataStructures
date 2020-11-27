class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            self.first = newNode
            newNode.next = temp
        self.size += 1
        return self

    def pop(self):
        if self.size == 0:
            return None
        popped = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        else:
            newHead = popped.next
            popped.next = None
            self.first = newHead
        self.size -= 1
        return popped.val

    def print(self):
        output = []
        if self.size != 0:
            current = self.first
            output.append(current.val)
            while current.next != None:
                current = current.next
                output.append(current.val)
        return output

    def getSize(self):
        return self.size
            
        
stack = Stack()
stack.push(5)
print(stack.print())
stack.push(6)
print(stack.print())
stack.push(7)
print(stack.print())
stack.push(8)
print(stack.print())
print(stack.pop())
print(stack.print())
print(stack.pop())
print(stack.print())
print(stack.pop())
print(stack.print())
print(stack.pop())
print(stack.print())