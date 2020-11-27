class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    push(val) {
        let newNode = new Node(val);
        if (this.size === 0) {
            this.first = newNode;
            this.last = newNode;
        } else {
            let first = this.first;
            newNode.next = first;
            this.first = newNode;
        }
        this.size += 1;
        return this.size;
    }

    pop() {
        if (this.size === 0) {
            return;
        } else if (this.size === 1) {
            var temp = this.first;
            this.first = null;
            this.last = null;
        } else {
            var temp = this.first;
            this.first = temp.next;
            temp.next = null;
        }
        this.size -= 1;
        return temp.val;
    }
}

let stack = new Stack()

console.log(stack.push('Hi'))
console.log(stack.push('There'))
console.log(stack.push('How'))
console.log(stack.push('Are You?'))
console.log(stack)
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())
console.log(stack.pop())