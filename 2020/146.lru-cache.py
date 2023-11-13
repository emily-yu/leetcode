#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

from collections import OrderedDict
# https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-+-Double-LinkedList/45368

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.vals = {} # { key: (val, Node) }
        self.lru = None # Node
        self.mru = None # Node

    def get(self, key: int) -> int:
        # go to vals[key][1]: 
        # 1) reassign prev and next to each other
        # 2) assign mru.next = vals[key][0]
        # return vals[key][0]

    def put(self, key: int, value: int) -> None:
        # get lru node: 1) pop from vals, 2) remove from array + reassign
        # add new node: 1) add to vals, 2) add as mru node + reassign pointers

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

