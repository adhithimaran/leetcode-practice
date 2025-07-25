def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    def helper(node):
        if not node:
            return 0  # Return 0 if the node is None
        
        # Recursively get the depth of the left and right subtrees
        left_depth = helper(node.left)
        right_depth = helper(node.right)
        
        # Return the max depth between the left and right subtrees plus 1 for the current node
        return max(left_depth, right_depth) + 1
    
    return helper(root)