# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        #create gap
        while n>0 and right:
            right = right.next
            n -= 1
        #move both untill right reaches end
        while right:
            left = left.next
            right = right.next
        # perform the removal
        left.next = left.next.next
        return dummy.next
        