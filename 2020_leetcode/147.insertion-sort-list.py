#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
            
        # # [4, 2, 1, 3]

        # def swap(head):
        #     temp = head.next # to 2
        #     head.next = temp.next # to 1
        #     temp.next = head
        #     return temp
        
        # # new = swap(head)

        # # print(new.val)

        length = 0
        lengthnode = head
        vals = []
        while lengthnode is not None:
            vals.append(lengthnode.val)
            length += 1
            lengthnode = lengthnode.next

        # print()
        # def getnode(ind):
        #     print("get node ", ind)
        #     trail = head

        #     if ind == 0:
        #         return trail

        #     # print("start")
        #     limit = ind # element to get
        #     ind = 0
        #     # while trail.next is not None:
        #     for i in range(limit):
        #         # print(ind, trail.val)

        #         if ind == limit:
        #             print('return', trail.val)
        #             return trail

        #         # print(trail.val)
        #         trail = trail.next
        #         ind += 1
        #     # print("end")
        #     return trail
                
        # # print('asdf: ', getnode(2).val)
        # # print('asdf: ', getnode(3).val)
        # print()

        # # print(vals)
        # # chain = head
        # # ind = 0
        # # for i in range(0, length):
        # #     # print(getnode(i).val)
        # #     print('backwards')
        # #     print(vals[:i])
        # #     print('value to put: ', vals[i])
        # #     for j in range(len(vals[:i])):
        # #         print(vals[i], vals[j])
        # #         if vals[i] < vals[j]:
        # #             print("done", j)

        # #             # swap here
        # #             new = swap(head)
        # #             # return new
        # #             break
        # #     print()


        # def swap2(head, ind1, ind2):
                
        #     # node1 = getnode(ind1)
        #     node1 = getnode(ind1)
        #     node2 = getnode(ind2)
        #     # print(node0, node1, node2)
        #     # print('...', ind1, ind2)
        #     if ind1-1 < 0:
        #         node1.next = node2.next
        #         node2.next = node1
        #         return

        #     node0 = getnode(ind1-1)
        #     if ind2 == length - 1:
        #         node0.next = node2
        #         node2.next = node1
        #         node1.next = None
        #         return

        #     node0.next = node2
        #     node1.next = node2.next
        #     node2.next = node1

        #     # print('???', node1.val, node2.val)
        #     return
        #     # return node0

        print("-------------------------------------")
        
        tail = head
        racer = head
        racerprev = head
        i = 0
        while tail is not None:
            tailelem = vals[i]
            print(tailelem)
            for j in range(i):
                child = vals[j]
                if child >= tailelem:
                    ## swap tail and racer
                    racerprev.next = tail
                    temp = racer.next
                    racer.next = tail.next
                    tail.next = temp
                    vals[i], vals[j] = vals[j], vals[i]
                else:
                    if i > 0:
                        racerprev = racer
                    racer = racer.next

            racer = head
            racerprev = None
            tail = tail.next
            i += 1
                    
        print()
        head2 = head
        # swap2(head, 2, 3)
        while head2 is not None:
            print(head2.val)
            head2 = head2.next

        # print(new.val)

        # new2 = new.next
        # new2 = swap(new2)

        # new.next = new2

        # new3 = new2.next
        # new3 = swap(new3)
        
        # new2.next = new3

        return head

# @lc code=end

