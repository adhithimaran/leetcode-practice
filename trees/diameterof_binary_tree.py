# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # Reset for each test case
        
        def height(node):
            if not node:
                return 0
            
            r = height(node.right)
            l = height(node.left)
            self.max_diameter = max(self.max_diameter, r + l)
            
            return max(r, l) + 1  # Return height, not diameter
        
        height(root)
        return self.max_diameter