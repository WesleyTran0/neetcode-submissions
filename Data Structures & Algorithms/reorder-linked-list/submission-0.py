# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        
        # 1 -> 7 -> 2 -> 6 -> 3 -> 5 -> 4


        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6

        # 1 -> 6 -> 2 -> 5 -> 3 -> 4
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the second half of the list. So 6 -> 5 -> 4 -> None
        # the front still points 1 -> 2 -> 3 ->  None 
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # prev ends up being the 2nd new elem of the list and also ends in the end of the list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next # store what will be list
            first.next = second # lose what will be lost
            second.next = tmp1 # and change the values to what they should point to
            first, second = tmp1, tmp2 # move to the next value pairs that will change
