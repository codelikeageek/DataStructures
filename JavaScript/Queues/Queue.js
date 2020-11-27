class Node {
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class Queue {
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }

    enqueue(val){
        let node = new Node(val);
        if (this.size === 0){
            this.first = node;
            this.last = node;
        }
        else {
            this.last.next = node;
            this.last = node;
        }
        this.size += 1;
        return this.size;
        
    }

    dequeue(){
        if(this.size === 0){
            return null;
        } 
        let temp = this.first;
        if (this.size === 1){
            this.first = null;
            this.last = null;
        }
        else {
            let newHead = temp.next;
            temp.next = null;
            this.first = newHead;
        }
        this.size -= 1;
        return temp.val;
    }
}

let q = new Queue()

console.log(q.enqueue("FIRST"))
console.log(q)
console.log(q.enqueue("SECOND"))
console.log(q)
console.log(q.enqueue("THIRD"))
console.log(q)
console.log(q.dequeue())
console.log(q)
console.log(q.dequeue())
console.log(q)
console.log(q.dequeue())
console.log(q)