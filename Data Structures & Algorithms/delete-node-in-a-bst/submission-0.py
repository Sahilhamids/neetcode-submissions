class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found! Handle the cases:
            
            # Case 1 & 2: Node has 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: Node has both children
            # Find the inorder successor (smallest value in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Copy the successor's value to this node
            root.val = curr.val
            
            # Delete the successor from the right subtree
            root.right = self.deleteNode(root.right, root.val)
            
        return root