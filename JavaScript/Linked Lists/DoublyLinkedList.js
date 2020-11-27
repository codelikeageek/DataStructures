class Node {
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class DoublyLinkedList {
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val){
        let node = new Node(val);
        if (this.length === 0) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
        this.length +=1;
        return this;
    }

    pop(){
        if (this.length === 0) {
            return
        }
        let node = this.tail;
        if (this.length === 1){
            this.head = null;
            this.tail = null;
        } else {
            this.tail = node.prev;
            this.tail.next = null;
            node.prev = null;
        }
        this.length -= 1;
        return node;
    }

    shift(){
        if (this.length === 0) {
            return;
        }
        let oldHead = this.head;
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = oldHead.next;
            this.head.prev = null;
            oldHead.next = null;
        }
        this.length -= 1;
        return oldHead;
    }

    unshift(val){
        let newNode = new Node(val);
        if (this.length === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length += 1;
        return  this;
    }

    get(idx){
        if (idx < 0 || idx >= this.length){
            return;
        } else if (idx === 0){
            return this.head;
        } else if (idx === this.length - 1){
            return this.tail;
        } else {
            let mid = Math.floor(this.length/2);
            if (idx <= mid){
                let counter = 0;
                let currentNode = this.head;
                while (counter < idx){
                    currentNode = currentNode.next;
                    counter += 1;
                }
                return currentNode;
            } else {
                let counter = this.length - 1;
                let currentNode = this.tail;
                while (counter > idx){
                    currentNode = currentNode.prev;
                    counter -= 1;
                }
                return currentNode;
            }
        }
    }

    set(idx, val) {
        let newNode = this.get(idx);
        if (newNode){
            newNode.val = val;
            return true;
        }
        return false;
    }

    insert(idx, val) {
        if (idx < 0 || idx > this.length){
            return false;
        }
        else if (idx === 0){
            let newNode = this.unshift(val);
            if (newNode){
                return true;
            } else {
                return false;
            }
        } else if (idx === this.length){
            let newNode = this.push(val);
            if (newNode){
                return true;
            } else {
                return false;
            }
        } else {
            let newNode = new Node(val);
            let preNode = this.get(idx-1);
            let postNode = preNode.next;
            preNode.next = newNode;
            newNode.prev = preNode;
            newNode.next = postNode;
            postNode.prev = newNode;
            this.length += 1;
            return true;
        }
    }

    remove(idx){
        if (idx < 0 || idx >= this.length){
            return;
        } else if (idx === 0){
            return this.shift();
        } else if (idx === this.length - 1){
            return this.pop();
        } else {
            let preNode = this.get(idx-1);
            let currentNode = preNode.next;
            let postNode = currentNode.next;
            postNode.prev = currentNode.prev;
            preNode.next = currentNode.next;
            currentNode.next = null;
            currentNode.prev = null;
            this.length -= 1;
            return currentNode;
        }
    }

    print(){
        let arr = [];
        let current = this.head;
        while(current){
            arr.push(current.val);
            current = current.next;
        }
        return arr;
    }

    reverse(){
        if (this.length === 1){
            return this; 
        } else {
            let node = this.head;
            this.head = this.tail;
            this.tail = node;
            let next = null;
            let prev = null;
            for(let i = 0; i < this.length; i++){
                next = node.next;
                node.next = prev;
                node.prev = next;
                prev = node;
                node = next;
            }
        }
        return this;
    }
}

let dll = new DoublyLinkedList();

dll.push(0);
dll.push(1);
dll.push(2);
dll.push(3);
dll.push(4);
dll.push(5);
console.log(dll.print())
console.log(dll.reverse())
console.log(dll.print())
//console.log(dll.remove(-6));
//console.log(dll.remove(100));
//console.log(dll.remove(5));
//console.log(dll.remove(0));
//console.log(dll.remove(2));
//console.log(dll.remove(1));
//console.log(dll);