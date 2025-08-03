class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root, root2):
            if not root:
                return True
            
            traverse(root.left, root2.left)
            print(root.val)
            if (root.val != root2.val):
                return False
            traverse(root.right, root2.right)
        
        return self.traverse(p, q)
    




