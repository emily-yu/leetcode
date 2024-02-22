#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        """
        [note] intent
        - practice #1: translate written req into process for interviewer
        - issue in prior interviews is that i'm op at whiteboarding but suck at online coding
        - next step - record myself talking and then critique
        input: 
        - we get LIST of UNSORTED stones 
        operation
            iterate on stones
                get two larget stones
                perform calculation
                remove two used stones
                put new value in
            when there's one stone left, return
        output
        1. one value of stones
        2. no stones = y-x of last two is 0
        edge cases
        - no stones 
        - one stone: no y-x operation
        - two stones: if equal, then 0. else can perform operation
        
        example
        note, sort default complexity = nlogn
        [2,7,4,1,8,1]
        -
        heaviest 2: 8 and 7
        [2, x, 4, 1, x, 1] & 8-7=1
        insert 1 into SOMEWHERE [2, 4, 1, 1]
        [2, 4, 1, 1, 1]
        - 
        heaviest 2: 4 and 2
        [x, x, 1, 1, 1] and 4-2=2
        insert 2 into SOMEWHERE [1, 1, 1]
        [2, 1, 1, 1]
        -
        [x, x, 1, 1] and 2-1=1
        [1, 1, 1]
        -
        [x, x, 1] and 1-1=0 nothing
        [1] one stone is left:
                return 1 stone
            if no stones left:
                return 0 stone

        brute forcey
        1. go through nums
            var largest1
            if number is greater than largest1, largest2=largets1 & update largest1.
            if number is greater than largest2 only, update largest2.
        (now have 2 largest)
        2. calculate new rock
        3. assign new rock to one of the two 
        """

        # edge cases
        # if len(stones) == 2:
        #     return abs(stones[1] - stones[0])
        
        # # brute forcey
        # while len(stones) > 1:
        #     largest1 = -1
        #     largest2 = -1
        #      # find and track stones
        #     for i, num in enumerate(stones):
        #         print(i, num)
        #         if num > stones[largest1]:
        #             largest2 = largest1
        #             # largest1 = num
        #             largest1 = i
        #         elif num > stones[largest2]:
        #             # largest2 = num       
        #             largest2 = i       
        
        #     # # remove i2 stone, placed after bcz affects i1 assignment
        #     # # stones = stones[:i] + stones[i:] # check this op
        #     # stones.pop(i2) # https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
        #     # i2 = -999 # reset
        #     # print(stones) # check for the result
        #     largest2val, largest1val = stones.pop(largest2), stones.pop(largest1)
        #     # largest1val = stones.pop(largest1)

        #     calculation = abs(largest2val - largest1val)
        #     if calculation != 0:
        #         stones.append(calculation)
        #     print(stones)

        # # print(stones) # check for the result
        # if len(stones) == 0:
        #     return 0
        # if len(stones) == 1:
        #     return stones[0]

        # # work log
        # # 11:45am, runs but wrong output need to debug. 
        # # 1:55pm, this shit iterates over way too many times wtf, n^2 because it has to keep going over everything

        stones.sort() # pre-sort, nlogn

        while len(stones) > 2: 
            # calculate from last two elems
            largest = stones[-1]
            mid = stones[-2]
            new = largest-mid
            print("asdf", largest, mid, new, stones)
            # find place in arr
            for i in range(0, len(stones)):
                if new <= stones[i]:# or new == 0:
                    # prev = stones[:i]
                    # next = stones[i:len(stones)-2] # remove last two
                    # print(prev, next)
                    if new != 0:
                        stones = [new] + stones
                    # else:
                    stones = stones[:len(stones)-2]
                    stones.sort()
                    break

                print(stones)
    
        # when reaches <2 elements do calculation
        print(stones)
        if len(stones) == 2:
            return abs(stones[1] - stones[0])
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]



        
# @lc code=end

