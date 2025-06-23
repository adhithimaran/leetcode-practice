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
        
        real_to_copy = {}
        curr = head
        head_copy = None
        while curr:
            # make new node, set the value
            new_node = Node(curr.val, None, None)
            if curr is head:
                head_copy = new_node
            real_to_copy[curr] = new_node
            curr = curr.next
        # now we have a dict with OG nodes mapped to copies of only the values
            
        
        curr = head
        while curr:
            # set the next node and random to the new_nodes
            if curr.next:
                real_to_copy[curr].next = real_to_copy[curr.next]
            if curr.random:
                real_to_copy[curr].random = real_to_copy[curr.random]
            curr = curr.next
        return head_copy