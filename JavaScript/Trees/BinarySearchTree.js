class Node {
    constructor(val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }

    insert(val){
        let newNode = new Node(val);
        if(!this.root){
            this.root = newNode;
        } else {
            let current = this.root;
            while (true){
                if (newNode.val < current.val){
                    if (!current.left){
                        current.left = newNode;
                        break;
                    } else {
                        current = current.left;
                    }
                } else if (newNode.val > current.val){
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
        }
        return this;
    }

    find(val){
        if (!this.root){
            return;
        }
        else if (val === this.root.val){
            return this.root;
        }
        let current = this.root;
        while(true){
            //console.log(current.val)
            if (val < current.val){
                if (!current.left){
                    return;
                } else {
                    current = current.left;
                }
            } else if (val > current.val){
                if (!current.right){
                    return;
                } else {
                    current = current.right;
                } 
            } else {
                return current;
            }
        }
    }
}

let tree = new BinarySearchTree()

console.log(tree.insert(3))
console.log(tree.insert(5))
console.log(tree.insert(10))
console.log(tree.insert(2))
console.log(tree.find(10))
console.log(tree.find(3))
console.log(tree.find(2))
console.log(tree.find(5))
console.log(tree.find(0))

