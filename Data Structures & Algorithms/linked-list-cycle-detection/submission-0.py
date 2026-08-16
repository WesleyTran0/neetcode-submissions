# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        fast, slow = head, head

        while fast:
            fast = fast.next
            
            if not fast or not slow:
                return False
            
            if slow == fast:
                return True
            
            fast = fast.next
            slow = slow.next

        return False
