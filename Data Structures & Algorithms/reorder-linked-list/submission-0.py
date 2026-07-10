# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #step 1 find center node using floyds algorithm 
        #step 2 reverse list  from center node
        #step 3 merge 
        start = head
        slow=start
        fast=start

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow .next = None
        prev = None
        while tail:
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt

        #prev points to reversed start
        #merge

        while prev:
            temp1 = start.next
            temp2 = prev.next
            start.next = prev
            start = temp1
            prev.next = temp1
            prev = temp2
            

        




        


        