"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        head_copy.val = head.val
        head_copy.next = head.next
        head_copy.random = head.random
        
        curr = head
        curr_copy = head_copy
        while curr:
            curr_copy.val = curr.val
            curr_copy.next = curr.next
            curr_copy.random = curr.random

            curr = curr.next
            curr_copy = curr_copy.next
        return head_copy