from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is None:
                return True
            return False
        if q is None:
            if p is None:
                return True
            return False
        
        def traverse(root, root2):

            if not root and not root2:
                return True
            
            traverse(root.left, root2.left)
            print(root.val)
            if (root.val != root2.val):
                return False
            traverse(root.right, root2.right)
            return True
        
        return traverse(p, q)

# Test Cases
def run_tests():
    solution = Solution()
    
    # Test Case 1: Both trees are None (empty)
    print("Test 1: Both empty trees")
    result1 = solution.isSameTree(None, None)
    print(f"Result: {result1}")
    print("Expected: True\n")
    
    # Test Case 2: One tree is None, other is not
    print("Test 2: One empty, one non-empty")
    tree1 = TreeNode(1)
    result2 = solution.isSameTree(tree1, None)
    print(f"Result: {result2}")
    print("Expected: False\n")
    
    # Test Case 3: Single node trees with same value
    print("Test 3: Single nodes, same value")
    tree1 = TreeNode(1)
    tree2 = TreeNode(1)
    result3 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result3}")
    print("Expected: True\n")
    
    # Test Case 4: Single node trees with different values
    print("Test 4: Single nodes, different values")
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    result4 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result4}")
    print("Expected: False\n")
    
    # Test Case 5: Identical balanced trees
    print("Test 5: Identical balanced trees [1,2,3]")
    #     1       1
    #    / \     / \
    #   2   3   2   3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    
    result5 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result5}")
    print("Expected: True\n")
    
    # Test Case 6: Different structure, same values
    print("Test 6: Different structure [1,2] vs [1,null,2]")
    #   1       1
    #  /         \
    # 2           2
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    
    tree2 = TreeNode(1)
    tree2.right = TreeNode(2)
    
    result6 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result6}")
    print("Expected: False\n")
    
    # Test Case 7: Same structure, different values
    print("Test 7: Same structure, different values [1,2,1] vs [1,1,2]")
    #     1       1
    #    / \     / \
    #   2   1   1   2
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(1)
    
    tree2 = TreeNode(1)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(2)
    
    result7 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result7}")
    print("Expected: False\n")
    
    # Test Case 8: Deeper identical trees
    print("Test 8: Deeper identical trees")
    #       1           1
    #      / \         / \
    #     2   3       2   3
    #    /   / \     /   / \
    #   4   5   6   4   5   6
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.right.left = TreeNode(5)
    tree1.right.right = TreeNode(6)
    
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    tree2.left.left = TreeNode(4)
    tree2.right.left = TreeNode(5)
    tree2.right.right = TreeNode(6)
    
    result8 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result8}")
    print("Expected: True\n")
    
    # Test Case 9: Unbalanced trees (left skewed)
    print("Test 9: Left-skewed trees")
    #   1     1
    #  /     /
    # 2     2
    #/     /
    #3    3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(3)
    
    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.left.left = TreeNode(3)
    
    result9 = solution.isSameTree(tree1, tree2)
    print(f"Result: {result9}")
    print("Expected: True\n")

if __name__ == "__main__":
    run_tests()