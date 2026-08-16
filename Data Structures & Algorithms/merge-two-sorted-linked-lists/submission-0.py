# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        return_list = ListNode()
        dummy = return_list

        while list1 or list2:
            if not list1:
                # add from list2 & increment
                dummy.next = ListNode(list2.val, list2.next)
                break;
            elif not list2:
                # add from list1 & increment
                dummy.next = ListNode(list1.val, list1.next)
                break;
            else:
                # determine if list1 or list2 val is less and then add and increment them
                if list1.val < list2.val:
                    dummy.next = ListNode(list1.val, None)
                    dummy = dummy.next
                    list1 = list1.next
                else: 
                    dummy.next = ListNode(list2.val, None)
                    dummy = dummy.next
                    list2 = list2.next
            
        return return_list.next