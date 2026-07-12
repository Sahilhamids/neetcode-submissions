class Node:
    def __init__(self,key,val):
        self.key:int = key
        self.val:int = val
        self.freq:int = 1 #a node starts with a freq of one
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def remove_node(self,node:Node):
        # most recently used
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    def add_to_head(self, node:Node):
        # add node right after dummy head node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    def remove_tail(self) -> Node:
        if self.size == 0:
            return None
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity:int = capacity
        self.min_freq:int = 0
        self.key_map = {} # key as key and doubly linked list node as value
        self.freq_map = collections.defaultdict(DoublyLinkedList) # key as frequency and doubly list  as value
    
    def _update_freq(self, node:Node):
        #helper function
        old_freq = node.freq
        new_freq = old_freq + 1
        node.freq = new_freq
        # removo from old freq
        old_list = self.freq_map[old_freq]
        old_list.remove_node(node)
        # add to new freq
        new_list = self.freq_map[new_freq]
        new_list.add_to_head(node)
        # update min freq
        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq += 1
        
    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        value = node.val
        self._update_freq(node)

        return value

    def put(self, key: int, value: int) -> None:
        
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
        else:
            #check for size if yes then evict lfu
            if len(self.key_map) >= self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                evicted_node = lfu_list.remove_tail()
                if evicted_node:
                    del self.key_map[evicted_node.key]
            #create and insert new node
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1 #reset minimum freq to 1 for the newly inserted node


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)