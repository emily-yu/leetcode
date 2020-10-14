#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return []

        end = []

        tmp = head
        while (tmp != None):
            # print(tmp.val)

            end.append(tmp)
            if len(end) > (n + 1):
                end.pop(0) # pop the oldest element

            tmp = tmp.next
            # print(end)

        # print('...')
        # edge: if total # less than n
        if len(end) < n:
            return head

        # print("len: ", len(end))
        if len(end) >= 3: # n = 3
            prev = end.pop(0)
            pivot = end.pop(0)
            # print(n, len(end))
            if n == len(end) + 2: # after removing prev and pivot
                head = pivot
                return head

            # print("prev: ", prev.val)
            # print("pivot: ", pivot.val)
            prev.next = pivot.next
            pivot.next.prev = prev
        elif len(end) == 2: # n = 1
            prev = end.pop(0)
            if n == 1:
                prev.next = None
            if n == 2:
                head = prev.next
        elif len(end) == 1:
            return None

        return head
# @lc code=end

