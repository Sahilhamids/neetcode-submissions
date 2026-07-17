# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        curr1 = p
        curr2 = q
        def isSame(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            val1 = p.val
            val2 = q.val

            if val1 != val2:
                return False
            return isSame(p.left,q.left) and isSame(p.right,q.right)
        return isSame(curr1,curr2)
            
        