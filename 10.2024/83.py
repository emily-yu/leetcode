# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # exists = set()
        # prev = None
        first = head
        while head.next is not None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
            # exists.add(head.next)
            # head = head.next
        
        head = first
        return head
