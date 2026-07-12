# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        
        dummy = ListNode(0,head)
        prev = dummy
        
        for _ in range(left-1):
            prev = prev.next
        
        curr = prev.next
        prev_node = None
        for _ in range(right-left +1):
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        
        prev.next.next = curr
        prev.next = prev_node
        return dummy.next
        
        

            
            



            


