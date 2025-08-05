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
        
        return (self.isSameTree(root, subRoot) or 
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if not p and not q:
            return True
        if not p or not q:
            return False

        # Check current nodes and recurse on children
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
        

        