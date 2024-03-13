#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dict_randoms = {}
        prev = None
        node = head

        while node is not None:
            if node not in dict_randoms:
                dict[node] = Node(node.val, node.next, node.random) # (originalNode, original Node)


        # edge case
        if not head:
            return None

        d = {} # store randoms
        p = head

        while p: # for each original node
            d[p] = Node(p.val, None, None) # original node: copy of node
            p = p.next # next original node

        p = head # reset pointer to original node
        while p: # for each original node, set ranodm and next for the copies in the hashmap
            if p.random:
                d[p].random = d[p.random] # set copy.random in the dict to = original node that is the value of the mapped copy.random node
            if p.next:
                d[p].next = d[p.next] # set copy.next in the dict to the correct copy mapped from head.next
            p = p.next

        return d[head]
# @lc code=end

