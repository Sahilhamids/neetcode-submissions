# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        def is_identical(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            # If both are null, they are identical
            if not node1 and not node2:
                return True
            # If only one is null, or values don't match, they aren't identical
            if not node1 or not node2 or node1.val != node2.val:
                return False
            # Check both left and right subtrees
            return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)

        # Main traversal function to look for the subRoot
        def go_to(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            # If the current node matches the subRoot value, verify the full structure
            if node.val == subRoot.val:
                if is_identical(node, subRoot):
                    return True
            
            # Continue looking down the left and right branches
            return go_to(node.left) or go_to(node.right)

        return go_to(root)