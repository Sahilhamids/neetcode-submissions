# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        
        def invert_tree(node):
            if not node:
                return None
            node.left,node.right = node.right, node.left
            left_node = node.left
            right_node = node.right
            invert_tree(left_node)
            invert_tree(right_node)
            return 
        invert_tree(root)
        return root

            
        