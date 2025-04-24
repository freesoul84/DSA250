class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        if len(self.hashmap) == 0:
            self.hashmap.append([key,value])
        elif key not in [i[0] for i in self.hashmap if len(self.hashmap)>0]:
            self.hashmap.append([key,value])
        else:
            for i in range(len(self.hashmap)):
                if self.hashmap[i][0] == key:
                    self.hashmap[i][1] = value
        return self.hashmap
    
    def get(self, key: int) -> int:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                return self.hashmap[i][1]
        else:
            return -1
    
    def remove(self, key: int) -> None:
        length = len(self.hashmap)
        for i in range(length):
                if len(self.hashmap)>0:
                    if self.hashmap[i][0] == key:
                        del self.hashmap[i]
                        break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)