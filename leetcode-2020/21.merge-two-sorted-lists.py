#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            root = ListNode()
            head = root
            while (l1 is not None or l2 is not None):
                if l1 is not None and l2 is None:
                    root.next = l1
                    l1 = l1.next
                elif l1 is None and l2 is not None:
                    root.next = l2
                    l2 = l2.next
                else:
                    if l1.val <= l2.val:
                        root.next = l1
                        l1 = l1.next
                    else:
                        root.next = l2
                        l2 = l2.next
                root = root.next
            
            return head.next # pop out the unneeded placeholder
# @lc code=end

