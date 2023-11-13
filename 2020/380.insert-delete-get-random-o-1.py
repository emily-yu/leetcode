#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:
    data = set()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # check if set contains element
        if val in self.data:
            # yes - False
            return False

        # no - True, append to list
        self.data.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # check if set contains elem
        if val in self.data:
            # yes - True, remove
            self.data.remove(val)
            return True
        # no - False
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # if length == 1: return list[0]
        # if len(self.data) == 1:
        #     return list(self.data)[0]
        # # else:
        # else:
        #     # math.random from 0 to length-1
        #     # randomly call one element from list
        elem = random.sample(self.data, 1)[0]
        # self.data.remove(elem)
        # print(self.data)
        return elem
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

