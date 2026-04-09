# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # two pointer, one goes twice as fast, and if they at some point 
        # meet or cross, then there is a cycle
        curr = curr2 = head
        

        while curr and curr2 and curr2.next: 
            curr2 = curr2.next.next
            if curr == curr2:
                return True
            curr = curr.next
        return False