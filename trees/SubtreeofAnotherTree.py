# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursive approach

        # Input: 0 <= nodes of both trees <= 100

        # edges:
        # null root and null sub root -> True
        # null root and subroot -> False
        # root and null subroot -> True
        if not subRoot:
            return True
        if not root: # subroot will not be null if we get to this point
            return False
        
        # root and subroot -> Recursive Approach
            # iterate through both lists consecutively until root == subroot
            # check if next nodes match as well
            # YES? True
            # NO? False
        def rec_traverse(root, subRoot):
            # reach end of root
            # reach end of subroot
            # root != subroot: keep going
            # root == subroot: keep going and check each node for equality
            

            return True
        
        return rec_traverse(root, subRoot)
        

        