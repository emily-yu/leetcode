#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        Accepted
        16/16 cases passed (52 ms)
        Your runtime beats 50.93 % of python3 submissions
        Your memory usage beats 7.78 % of python3 submissions (17.8 MB)
        '''
        nodes = set()
        while head is not None:
            if head in nodes:
                return head

            nodes.add(head)
            head = head.next

        return None

# @lc code=end

