class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        self.size= 10000
        self.map = [ListNode() for _ in range(self.size)]
    
    def hash_(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hash_(key)
        curr = self.map[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr= curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        idx = self.hash_(key)
        curr = self.map[idx].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
    def remove(self, key: int) -> None:
        idx = self.hash_(key)
        curr = self.map[idx]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)