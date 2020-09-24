#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head

        root = head
        evenroot = head.next

        odd = head
        even = head.next
        temp = head

        isodd = True
        while odd.next is not None and even.next is not None:
            if isodd: 
                # print(odd.val, temp.val)
                temp = odd
                # print(temp)
                odd = even.next
                # print(odd)
                temp.next = odd
                # print(temp)
                temp = temp.next
                # print(temp)
                odd = temp
                # print(odd)
                isodd = False
            else:
                # print(even.val, temp.val)
                temp = even
                # print(temp)
                even = odd.next
                # print(even)
                temp.next = even
                # print(temp)
                temp = temp.next
                # print(temp)
                even = temp
                # print(even)
                isodd = True
            
            # print(odd.val, even.val)
            # print()

        even.next = None
        odd.next = evenroot
        return head
# @lc code=end

