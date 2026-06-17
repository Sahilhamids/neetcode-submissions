class MyHashSet:

    def __init__(self):
        self.size=10000
        self.table=[[]for _ in range(self.size)]
    def hash_(self, key:int)-> int:
        return key % self.size
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.table[self.hash_(key)].append(key)
            
    def remove(self, key: int) -> None:
        idx= self.hash_(key)
        if key in self.table[idx]:
            self.table[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx= self.hash_(key)
        return key in self.table[idx]
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)