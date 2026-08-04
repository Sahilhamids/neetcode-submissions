class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Step 1: Recursively visit left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # Step 2: Check if current node is now a leaf and matches the target
        if not root.left and not root.right and root.val == target:
            return None
            
        # Step 3: Otherwise, keep the node
        return root