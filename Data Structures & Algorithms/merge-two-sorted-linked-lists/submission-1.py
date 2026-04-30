# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        if not head1 and head2:
            return head2
        elif head1 and not head2:
            return head1
        else:
            dummy = head = ListNode()
            while head1 and head2:
                if head1.val < head2.val:
                    dummy.next = head1
                    head1 = head1.next
                else:
                    dummy.next = head2
                    head2 = head2.next
                dummy = dummy.next

            dummy.next = head2 if not head1 else head1

        return head.next

                
            
            