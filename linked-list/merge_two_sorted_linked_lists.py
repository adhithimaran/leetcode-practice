# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if (list1.val < list2.val):
            merge_list = list1
            list1 = list1.next
        else:
            merge_list = list2
            list2 = list2.next
        
        iter1 = list1
        iter2 = list2

        head = merge_list

        while (iter1 and iter2):
            if (iter1.val < iter2.val):
                merge_list.next = iter1
                merge_list = merge_list.next
                iter1 = iter1.next
            else:
                merge_list.next = iter2
                merge_list = merge_list.next
                iter2 = iter2.next
        if iter1:
            merge_list.next = iter1
        else:
            merge_list.next = iter2
        return head