class HashTable {
    constructor(size) {
        this.keyMap = new Array(size);
    }

    _hash(key) {
        let total = 0;
        let WEIRD_PRIME = 53;
        for (let i = 0; i < Math.min(key.length, 100); i++) {
            let char = key[i];
            let value = char.charCodeAt(0) - 96;
            total = (total * WEIRD_PRIME + value) % this.keyMap.length;
        }
        return total;
    }

    set(key, value) {
        let hash = this._hash(key);
        if (!this.keyMap[hash]) {
            this.keyMap[hash] = [];
        }
        this.keyMap[hash].push([key, value]);
        return this.keyMap;
    }

    get(key) {
        let hash = this._hash(key);
        if (this.keyMap[hash]) {
            for (let i = 0; i < this.keyMap[hash].length; i++) {
                if (this.keyMap[hash][i][0] === key) {
                    return this.keyMap[hash][i][1];
                }
            }
        }
        return;
    }

    keys() {
        let keysArr = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    if (!keysArr.push(this.keyMap[i][j][0])) {
                        keysArr.push(this.keyMap[i][j][0]);
                    }
                }
            }
        }
        return keysArr;
    }

    values() {
        let valuesArr = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    if (!valuesArr.includes(this.keyMap[i][j][1])) {
                        valuesArr.push(this.keyMap[i][j][1]);
                    }
                }
            }
        }
        return valuesArr;
    }
}

let map = new HashTable(13);
console.log(map.set("pink", "#ff3092"));
console.log(map.set("blue", "#a03e5c"));
console.log(map.set("green", "#bb3092"));
console.log(map.set("cyan", "#ae3e5f"));
console.log(map.set("black", "#6fc092"));
console.log(map.set("white", "#a69c5v"));
console.log(map.set("orange", "#ffe354"));
console.log(map.set("yellow", "#00ff5c"));
console.log(map.set("maroon", "#00ff5c"));
console.log(map.get("green"));
console.log(map.get("pink"));
console.log(map.get("orange"));
console.log(map.get("cyan"));
console.log(map.get("blue"));
console.log(map.get("yellow"));
console.log(map.get("sky"));
console.log(map.keys());
console.log(map.values());