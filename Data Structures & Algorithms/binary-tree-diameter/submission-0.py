# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        max_diameter = 0

        def find_diameter(root):
            nonlocal max_diameter
            if not root:
                return 0
            
            left_height = find_diameter(root.left)
            right_height = find_diameter(root.right)

            max_diameter = max( max_diameter , left_height + right_height)

            return 1 + max(left_height,right_height)

        #call function
        find_diameter(root)
        return max_diameter
        