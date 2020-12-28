#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # pivotq = []
        # netmax = 0
        # tracking = [0] * len(s)

        # pivot = None
        # count = 0
        # gap = 0 # replacements

        # while there are pivots to process / not end of arr
            # get pivot

            # iterate until gap is reached
                # if change in character, add to pivot & add to gap
                # if no change, just add to count
            
            # when gap is reached, compare netmax
            # reset
        
        '''
        approach 1; iterate over arr
        index = 0
        (A,0)
        > i=1, C: gap = 1, add(C, 1), count = 1
        > i=2, B: gap = 2, add(B, 2), count = 2
        > i=3, A: A == A, count = 3
        > i=4, A: A == A, count = 4
        > i=5, C: gap = 3 [stop] add (C, 5) as next pivot
        {
            1: C
            2: B
        }
        end=5, only add end-1 and end-2
        [(C, 5)]
        ...
        index = 0
        (A,0)
        > i=1, C: gap = 1, add(C, 1), count = 1
        > i=2, A: A == A, count = 3
        > i=3, A: A == A, count = 4
        > i=4, B: gap = 2, add(B, 4), count = 2
        > i=5, C: gap = 3 [stop] add (C, 5) as next pivot
        {
            1: C
            4: B
        }
        end=5, only add end-1 and end-2
        [(B, 4), (C, 5)]

        (C, 5)
        > i=6, B: gap = 1
        > i=7, B: gap = 2
        > i=8, 
        ...
        index = 5
        (C, 5)
        > i=6, C: count = 1
        
        i == len(s) - 1 return netmax


        approach 2; tuple sorting
        (A, 1)(C, 1)(B, 1)(A, 2)(C, 2)(B, 6)
        
        (A, 1)
        > (C, 1)... gap = 1
        > (B, 1)... gap = 2
        > (A=A, 2)
        > (C, 2)... gap = 4 > 2 [done]
        end; count = 3
        (C, 1)
        > (B, 1)... gap = 1
        > (A, 2)... gap = 3 > 2 [done]
        end; count = 1

        (B, 1)
        > (A, 2)... gap = 2
        > (C, 2)... gap = 4 > 2 [done]
        end; count = 1

        (B, 6)
        end; count = 6

        '''
        q = []
        prev = s[0]
        prevind = 0
        for i in range(1, len(s)):
            if s[i] != prev:
                # print(prev, i-prevind)
                q.append((prev, i-prevind))
                prev = s[i]
                prevind = i
            if i == len(s) - 1:
                # print(s[i], i-prevind+1)
                q.append((s[i], i-prevind+1))

        print(q)         

        tracking = {}
        for ind, elem in enumerate(q):
            print(ind, elem)
            if elem[0] in tracking:
                tracking[elem[0]].append(ind)
            else:
                tracking[elem[0]] = [ind]

        print(tracking)

        currmax = 0
        for ind, elem in enumerate(q):
            print(ind, elem)

            count = 0
            gap = 0
            for i in range(ind, len(q)):
                print(q[i], count)


                # print(q[i][0], elem[0], elem[1])
                if q[i][0] == elem[0]:
                    count += q[i][1]
                else:
                    gap += q[i][1]
                    if gap > k:
                        print("ct of: ", elem, ", ", count)
                        if count > currmax:
                            currmax = count
                        count = 0
                        break
                    count += q[i][1]
                print("count: ", count, ' gap: ', gap)

            if count > currmax:
                currmax = count
            print()
        return currmax
# @lc code=end

