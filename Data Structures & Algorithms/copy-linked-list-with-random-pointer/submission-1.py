"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        h_map = {}

        #first pass to create node copies wit values in new nodes old node as key new node as value
        curr = head
        while curr:
            h_map[curr] = Node(curr.val)
            curr = curr.next

        #second pass 
        curr = head
        while curr:
            #get new node created for the current old node
            newNode = h_map[curr]

            #link next and random using hash map
            newNode.next = h_map.get(curr.next)
            newNode.random = h_map.get(curr.random)
            curr = curr.next
        return h_map[head]
        
        