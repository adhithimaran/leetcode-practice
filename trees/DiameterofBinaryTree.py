# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # iterate through each node dfs and calc left and right heigh, sum toegther and update max var if needed
        if not root:
            return 0
        r = self.diameterOfBinaryTree(root.right)
        l = self.diameterOfBinaryTree(root.left)
        self.max_diameter = max(self.max_diameter, r+l)

        return self.max_diameter