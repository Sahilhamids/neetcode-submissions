# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []

        def in_order(root):
            nonlocal ls
            if not root:
                return 
            in_order(root.left)
            ls.append(root.val)
            in_order(root.right)
        in_order(root)
        return ls
        