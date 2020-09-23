#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        while head.next is not None:
            first = head
            second = head.next

            first.next = second.next
            second.next = first

            print(head.val)
            head = head.next.next

        return head

# @lc code=end

