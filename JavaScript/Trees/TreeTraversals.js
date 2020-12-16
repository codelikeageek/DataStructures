class ListNode {
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
        let newNode = new ListNode(val);
        if (this.size === 0){
            this.first = newNode;
            this.last = newNode;
        } else {
            let temp = this.last;
            temp.next = newNode;
            this.last = newNode;
        }
        this.size += 1;
        return this.size;   
    }

    dequeue(){
        if (!this.first){
            return;
        }
        let temp = this.first;
        if (this.size === 1){
            this.first = null;
            this.last = null;
        } else {
            let next = temp.next;
            temp.next = null;
            this.first = next;
        }
        this.size -= 1;
        return temp.val;
    }
}

class Node {
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Tree {
    constructor(){
        this.root = null;
    }
    
    insert(val){
        let newNode = new Node(val);
        if (this.root === null){
            this.root = newNode;
            return this;
        } 
        let current = this.root;
        while(true){
            if(val < current.val){
                if (!current.left){
                    current.left = newNode;
                    break;
                } else {
                    current = current.left;
                }
            } else if (val > current.val){
                if (!current.right){
                    current.right = newNode;
                    break;
                } else {
                    current = current.right;
                }
            } else {
                return;
            }
        }
        return this;
    }

    bfsTraversal(){
        let q = new Queue();
        let final = [];

        if(this.root === null){
            return final;
        } else {
            q.enqueue(this.root);
        }
        while(q.size != 0){
            let current = q.dequeue();
            console.log(final);
            final.push(current.val);
            if (current.left){
                q.enqueue(current.left);
            }
            if (current.right){
                q.enqueue(current.right);
            }
        }
        return final;
    }

    dfsPreOrder(){
        var final = [];
        let current = this.root;

        function traverse(node){
            final.push(node.val);
            if(node.left){
                traverse(node.left);
            }
            if(node.right){
                traverse(node.right)
            }
        }
        traverse(current);
        return final;
    }

    dfsPostOrder(){
        var final = [];
        let current = this.root;

        function traverse(node){
            if(node.left){
                traverse(node.left);
            }
            if(node.right){
                traverse(node.right)
            }
            final.push(node.val);
        }
        traverse(current);
        return final;
    }

    dfsInOrder(){
        var final = [];
        let current = this.root;

        function traverse(node){
            if(node.left){
                traverse(node.left);
            }
            final.push(node.val);
            if(node.right){
                traverse(node.right)
            }
        }
        traverse(current);
        return final;
    }
}



let bst = new Tree();

console.log(bst.insert(10));
console.log(bst.insert(2));
console.log(bst.insert(5));
console.log(bst.insert(3));
console.log(bst.insert(15));
console.log(bst.insert(18));
console.log(bst.insert(1));
console.log(bst.insert(6));
console.log(bst.insert(12));
console.log(bst.insert(14));
console.log(bst.insert(0));
console.log(bst.bfsTraversal());
console.log(bst.dfsPreOrder());
console.log(bst.dfsPostOrder());
console.log(bst.dfsInOrder());
//                  10
//          2               15 
//      1       5       12      18
//   0       3     6       14