# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n= len(preorder)

        def build(pl,pr,il,ir):
            if pl>pr:
                return None
            
            val = preorder[pl]
            mid = inorder.index(val,il,ir+1)
            root = TreeNode(val)
            lsize = mid - il
            root.left = build(pl+1,pl+lsize, il, mid-1)
            root.right = build(pl+lsize+1, pr, mid+1, ir)
            return root
        return build(0,n-1,0,n-1)        
        