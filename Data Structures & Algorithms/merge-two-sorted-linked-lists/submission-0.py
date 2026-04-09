# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # iterate through both list, and check to see which is less
        # and then keep or change pointer depending on the 
        # result

        newhead = temphead = ListNode()

        while list1 or list2:
            if not list1: 
                temphead.next = list2
                return newhead.next
            if not list2:
                temphead.next = list1
                return newhead.next
            if list1.val <= list2.val:
                temphead.next = list1
                list1 = list1.next
            else: 
                temphead.next = list2
                list2 = list2.next
            temphead = temphead.next
        return newhead.next