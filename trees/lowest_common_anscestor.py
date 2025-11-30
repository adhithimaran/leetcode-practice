# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p and q can be desc of itself
        # where split occurs (cannot be lower, will be higher)
        # iterate through each node
            # if p and q is less than curr -> left
            # if p and q ar greater than curr -> right
            # else:(one is lower and one is higher) this is the split, this is the lowest common ancestor
            # if p or q is equal to curr, this is the lowest common ancestor
        curr = root
        print(f'p:{p.val}')
        print(f'q:{q.val}')
        while curr:
            print(f'curr node:\n{curr.val}')
            if (p.val == curr.val) or (q.val == curr.val):
                return curr
            if ((p.val < curr.val) and (q.val > curr.val)) or ((p.val > curr.val) and (q.val < curr.val)):
                return curr
            if (p.val < curr.val) and (q.val < curr.val):
                curr = curr.left
            elif (p.val > curr.val) and (q.val > curr.val):
                curr = curr.right

# Test cases for lowestCommonAncestor method

def create_tree_1():
    """
    Creates BST:
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
    """
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    return root

def create_tree_2():
    """
    Creates simple BST:
      2
     /
    1
    """
    root = TreeNode(2)
    root.left = TreeNode(1)
    return root

def create_tree_3():
    """
    Creates single node BST:
    1
    """
    return TreeNode(1)

def create_tree_4():
    """
    Creates linear BST:
    1
     \
      2
       \
        3
         \
          4
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    return root

def test_lowest_common_ancestor():
    solution = Solution()
    
    # Test Case 1: Standard BST, LCA is internal node
    tree1 = create_tree_1()
    p1 = tree1.left  # node with value 2
    q1 = tree1.right  # node with value 8
    result1 = solution.lowestCommonAncestor(tree1, p1, q1)
    print(f"Test 1 - Expected: 6, Got: {result1.val if result1 else None}")
    
    # Test Case 2: Standard BST, LCA is one of the target nodes
    tree2 = create_tree_1()
    p2 = tree2.left  # node with value 2
    q2 = tree2.left.right  # node with value 4
    result2 = solution.lowestCommonAncestor(tree2, p2, q2)
    print(f"Test 2 - Expected: 2, Got: {result2.val if result2 else None}")
    
    # Test Case 3: Both nodes in left subtree
    tree3 = create_tree_1()
    p3 = tree3.left.left  # node with value 0
    q3 = tree3.left.right.right  # node with value 5
    result3 = solution.lowestCommonAncestor(tree3, p3, q3)
    print(f"Test 3 - Expected: 2, Got: {result3.val if result3 else None}")
    
    # Test Case 4: Both nodes in right subtree
    tree4 = create_tree_1()
    p4 = tree4.right.left  # node with value 7
    q4 = tree4.right.right  # node with value 9
    result4 = solution.lowestCommonAncestor(tree4, p4, q4)
    print(f"Test 4 - Expected: 8, Got: {result4.val if result4 else None}")
    
    # Test Case 5: Two-node tree
    tree5 = create_tree_2()
    p5 = tree5  # node with value 2
    q5 = tree5.left  # node with value 1
    result5 = solution.lowestCommonAncestor(tree5, p5, q5)
    print(f"Test 5 - Expected: 2, Got: {result5.val if result5 else None}")
    
    # Test Case 6: Single node tree (p and q are same node)
    tree6 = create_tree_3()
    p6 = tree6  # node with value 1
    q6 = tree6  # same node with value 1
    result6 = solution.lowestCommonAncestor(tree6, p6, q6)
    print(f"Test 6 - Expected: 1, Got: {result6.val if result6 else None}")
    
    # Test Case 7: Linear tree (right-skewed)
    tree7 = create_tree_4()
    p7 = tree7  # node with value 1
    q7 = tree7.right.right.right  # node with value 4
    result7 = solution.lowestCommonAncestor(tree7, p7, q7)
    print(f"Test 7 - Expected: 1, Got: {result7.val if result7 else None}")
    
    # Test Case 8: Linear tree, intermediate nodes
    tree8 = create_tree_4()
    p8 = tree8.right  # node with value 2
    q8 = tree8.right.right  # node with value 3
    result8 = solution.lowestCommonAncestor(tree8, p8, q8)
    print(f"Test 8 - Expected: 2, Got: {result8.val if result8 else None}")
    
    # Test Case 9: Deep nodes in complex tree
    tree9 = create_tree_1()
    p9 = tree9.left.right.left  # node with value 3
    q9 = tree9.left.right.right  # node with value 5
    result9 = solution.lowestCommonAncestor(tree9, p9, q9)
    print(f"Test 9 - Expected: 4, Got: {result9.val if result9 else None}")
    
    # Test Case 10: Root as one of the nodes
    tree10 = create_tree_1()
    p10 = tree10  # root node with value 6
    q10 = tree10.left.left  # node with value 0
    result10 = solution.lowestCommonAncestor(tree10, p10, q10)
    print(f"Test 10 - Expected: 6, Got: {result10.val if result10 else None}")

# Edge case considerations:
# - The algorithm assumes it's a BST but uses node comparison instead of value comparison
# - This will likely cause errors since you can't compare TreeNode objects with < or >
# - Should compare p.val and q.val with curr.val instead
# - The logic for checking if nodes are on different sides needs to use values, not nodes

if __name__ == "__main__":
    test_lowest_common_ancestor()