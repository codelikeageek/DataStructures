class HashTable:
    def __init__(self, size):
        self.keyMap = [None] * size

    def _hash(self, key):
        total = 0
        WEIRD_PRIME = 53
        for i in range(0, min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96
            total = (total * WEIRD_PRIME + value) % len(self.keyMap)
        return total

    def set(self, key, value):
        hash = self._hash(key)
        if self.keyMap[hash] == None:
            self.keyMap[hash] = []
        self.keyMap[hash].append([key, value])
        return self.keyMap


    def get(self, key):
        hash = self._hash(key)
        if self.keyMap[hash] == None:
            return None
        else:
            for i in range(0, len(self.keyMap[hash])):
                if self.keyMap[hash][i][0] == key:
                    return self.keyMap[hash][i][1]
        return None

    def keys(self):
        keysArr = []
        for i in range(0, len(self.keyMap)):
            if self.keyMap[i] != None:
                for j in range(0, len(self.keyMap[i])):
                    keysArr.append(self.keyMap[i][j][0])
        return keysArr

    def values(self):
        valuesArr = []
        for i in range(0, len(self.keyMap)):
            if self.keyMap[i] != None:
                for j in range(0, len(self.keyMap[i])):
                    valuesArr.append(self.keyMap[i][j][1])
        return valuesArr

map = HashTable(13)
print(map.set("pink", "#ff3092"))
print(map.set("blue", "#a03e5c"))
print(map.set("green", "#bb3092"))
print(map.set("cyan", "#ae3e5f"))
print(map.set("black", "#6fc092"))
print(map.set("white", "#a69c5v"))
print(map.set("orange", "#ffe354"))
print(map.set("yellow", "#00ff5c"))
print(map.set("maroon", "#00ff5c"))
print(map.get("green"))
print(map.get("pink"))  
print(map.get("orange"))
print(map.get("cyan"))
print(map.get("blue"))
print(map.get("yellow"))
print(map.get("sky"))
print(map.keys())
print(map.values())
