# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.d = 0
    
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        right = self.dfs(root.right)
        left = self.dfs(root.left)
        self.d = max(self.d, right + left)
        
        return 1 + max(right,left)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.d