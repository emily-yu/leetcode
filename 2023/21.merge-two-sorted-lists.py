#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ### brute force solution
        # eval head node first
        head = ListNode() # nothing
        ret = head

        while list1 is not None and list2 is not None:
            # add list1 node 
            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                head = head.next

                if list1.val == list2.val: # add list2 after list1
                    head.next = ListNode(list2.val) # add list1 node
                    list2 = list2.next #inc
                    head = head.next

                list1 = list1.next #inc

            elif list1.val > list2.val: # add list2 only
                head.next = ListNode(list2.val) # add list2 node
                list2 = list2.next #inc
                head = head.next

        if list1 is not None: 
            head.next = list1
        elif list2 is not None:
            head.next = list2

        return ret.next
        
        
# @lc code=end

