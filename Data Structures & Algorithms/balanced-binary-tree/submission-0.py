# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def find_height(root):
            if not root:
                return 0
            left = find_height(root.left)
            if left == -1:
                return -1
            right = find_height(root.right)
            if right == -1:
                return -1
            if abs(left -right) > 1:
                balanced = False
                return -1
            return 1 + max( left ,right )
        return find_height(root) != -1





