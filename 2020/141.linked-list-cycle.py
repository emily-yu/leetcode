#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # situations: 1) duplicate values, 1) has cycle, 2) doesn't have cycle, 3) one element or zero elements
        nodes = set()
        
        # for each node, add to hashmap, until == .next = null meaning found an end
        while (head is not None):
            print(head)
            if head in nodes:
                return True
            else:
                nodes.add(head)
            head = head.next
        return False
# @lc code=end

