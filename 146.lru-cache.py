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
        self.q = OrderedDict()
        self.limit = capacity

    def get(self, key: int) -> int:
        if key in self.q:
            val = self.q[key]
            del self.q[key] # remove, then reappend to put in correct order
            self.q[key] = val
            return val # return the val to get
        return -1 # doesn't exist

    def put(self, key: int, value: int) -> None:
        # # if already in, remove+reappend to put at most recent position
        # if key in self.q:
        #     del self.q[key]
        #     self.q[key] = value

        # # will exceed limit when adding one more element
        # elif len(self.q) >= self.limit:
        #     # oldkey, oldval = list(self.q)[0] # oldest at top
        #     # del self.q[oldkey]

        #     k, v = self.q.iteritems().next()
        #     print(k, v)
        #     del self.q[k]
        
        #     # append new element
        #     self.q[key] = value

        if key in self.q:
            # Delete existing key before refreshing it
            del self.q[key]
        elif len(self.q) >= self.limit:
            # Delete oldest
            k, v = self.q.iteritems().next()
            del self.q[k]
        self.q[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

