# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        dups = []
        while curr: 
            if curr not in dups:
                dups.append(curr)
                curr = curr.next
            else:
                return True
        print(dups)
        return False

