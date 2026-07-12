class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to front (MRU)
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node before updating
            self.remove(self.cache[key])
        
        # Create and add new node
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)
        
        # Evict if over capacity
        if len(self.cache) > self.capacity:
            # LRU node is just before the dummy tail
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]

    def add(self, node):
        # Insert right after head
        next_node = self.head.next
        node.prev = self.head
        node.next = next_node
        self.head.next = node
        next_node.prev = node

    def remove(self, node):
        # Disconnect node
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node