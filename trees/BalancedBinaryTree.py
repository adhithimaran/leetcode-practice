from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        right_h = self.getHeightRec(root, 'r')
        left_h = self.getHeightRec(root, 'l')

        print(f'right height: \n{right_h}')
        print(f'left height: \n{left_h}')

        if abs(left_h - right_h) > 1:
            return False
        

        self.isBalanced(root.right)
        self.isBalanced(root.left)


    def getHeightRec(self, root: Optional[TreeNode], right_or_left) -> int:
        if not root:
            return 0
        if right_or_left == 'r':
            return self.getHeightRec(root.right, 'r') +1
        if right_or_left == 'l':
            return self.getHeightRec(root.left, 'l') +1

def create_tree_from_list(values):
    """Create a binary tree from a list (level-order traversal)"""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def print_tree(root, level=0, prefix="Root: "):
    """Print tree structure for visualization"""
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Balanced tree [3,9,20,null,null,15,7]
    print("Test Case 1: Balanced tree")
    tree1 = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    print_tree(tree1)
    result1 = solution.isBalanced(tree1)
    print(f"Result: {result1}")
    print(f"Expected: True\n")
    
    # Test Case 2: Unbalanced tree [1,2,2,3,3,null,null,4,4]
    print("Test Case 2: Unbalanced tree")
    tree2 = create_tree_from_list([1, 2, 2, 3, 3, None, None, 4, 4])
    print_tree(tree2)
    result2 = solution.isBalanced(tree2)
    print(f"Result: {result2}")
    print(f"Expected: False\n")
    
    # Test Case 3: Empty tree
    print("Test Case 3: Empty tree")
    tree3 = None
    print("Tree: None")
    result3 = solution.isBalanced(tree3)
    print(f"Result: {result3}")
    print(f"Expected: True\n")
    
    # Test Case 4: Single node
    print("Test Case 4: Single node")
    tree4 = create_tree_from_list([1])
    print_tree(tree4)
    result4 = solution.isBalanced(tree4)
    print(f"Result: {result4}")
    print(f"Expected: True\n")