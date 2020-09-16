#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None: # edge case, one is empty
            return None

        lenA = 0
        frontA = headA
        while (headA.next != None):
            lenA += 1
            headA = headA.next
        print(headA.val)

        lenB = 0
        frontB = headB
        while (headB.next != None):
            lenB += 1
            headB = headB.next
        print(headB.val)

        if (headA != headB): # doesn't intersect, end vals not same
            return None
        else: # find the intersection, using original heads frontA, frontB
            # equalize the two arrays (eliminate the extra nodes from longer list)
            while (lenA != lenB):
                if (lenA > lenB):
                    frontA = frontA.next
                    lenA -= 1
                elif (lenB > lenA):
                    frontB = frontB.next
                    lenB -= 1
            while (frontA != frontB):
                frontA = frontA.next
                frontB = frontB.next
            return frontA

        print("continue, len: ", lenA, lenB, " values: ", frontA.val, frontB.val)
        
# @lc code=end

