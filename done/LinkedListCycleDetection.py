# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedListCycleDetection:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        visited = []
        ptr = head
        while ptr:
            if ptr in visited:
                return True
            visited.append(ptr)
            ptr = ptr.next
        return False