# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return: T/F
        # iterate through list 
        # check if node is in temp holding array
            # then true
        # else: continue and add node
        # add each node to array for cycle checking
        if (head.next == None):
            return False
        fast = head
        slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



    


        