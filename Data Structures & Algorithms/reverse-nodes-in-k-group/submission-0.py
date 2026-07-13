# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr =head
        count = 0
        while curr:
            count+=1
            curr = curr.next

        start = head
        node = head
        prev = dummy

        for i in range(0,count // k):
            new_head , new_tail = self.reverse_nodes(node, k)
            if i == 0:
                start = new_head
            node = new_tail.next
            prev.next = new_head
            prev = new_tail  
        return start

    def reverse_nodes(self, node, k)-> (Optional[ListNode],Optional[ListNode]):
            pre = None
            cur = node
            c = k 
            while cur and c:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                c -= 1

            new_head = pre
            new_tail = node
            new_tail.next = cur

            return ( new_head , new_tail)

        