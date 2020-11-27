class Node {
    constructor(val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class Deque {
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    addFront(val){
        let newNode = new Node(val);
        if (this.size == 0){
            this.first = newNode;
            this.last = newNode;
        } else {
            this.first.prev = newNode;
            newNode.next = this.first;
            this.first = newNode;
        }
        this.size += 1;
        return this;
    }

    addRear(val){
        let newNode = new Node(val);
        if (this.size == 0){
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            newNode.prev = this.last;
            this.last = newNode;
        }
        this.size += 1;
        return this;
    }

    removeFront(){
        if (this.size == 0){
            return;
        }
        let popped = this.first;
        if (this.size == 1){
            this.first = null;
            this.last = null;
        } else {
            let newHead = popped.next;
            newHead.prev = null;
            popped.next = null;
            this.first = newHead;
        }
        this.size -= 1;
        return popped.val;
    }

    removeRear(){
        if (this.size == 0){
            return;
        }
        let popped = this.last;
        if (this.size == 1){
            this.first = null;
            this.last = null;
        } else {
            let newTail = popped.prev;
            newTail.next = null;
            popped.prev = null;
            this.last = newTail;
        }
        this.size -= 1;
        return popped.val;
    }

    getSize(){
        return this.size;
    }

    printDeque(){
        let output = []
        let size = this.size;
        let current = this.first;
        while (size > 0){
            output.push(current.val);
            current = current.next;
            size -= 1;
        }
        return output;
    }
}
