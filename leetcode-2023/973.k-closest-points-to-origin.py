#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        """
        input: [(x, y)]
            - answer is unique = each dist is unique
        output: SMALLEST numbers k of (x1, y1) and (x2, y2) 
            - audit, overlooked that x2y2 is always (0,0) so we don't need to do so much calculation
        brute force
            op=rank so we have k top 
            brute {
                (i,j): ((i2, j2), dist)
            }
            better {
                key=dist : vals 
            }
            - ranking is .keys()

            op=iterate over every combination of points, calculate 
            brute
                var smallestDist
                for each point i in points: 
                    for each point j in points: 
                        combination of i & j
            better
                note=no need to do calucations, just x^2 + y^2 and compare
                example
                    points = [[3,3],[5,-1],[-2,4]], k = 2
                    [0, 0, 0]
                    [9, 26, 20] o(n)
                        need to rank by index: vals to be key because auto sorted
                        {
                            9: [index=0, index=n]
                            20: index=2
                            26: index=1
                        }
                    [9, 20, 26] rank.keys().sort() o(nlogn)
                    [9, 20]
                        if k=2, first 2 elements
                        rank.keys().sort()[0:2]
                        edge is if k > # elements
                    {
                        9: index=0 - (3,3)
                        20: index=2 - (-2,4)
                    }
        (25mins)
        """
        rank = {}
        for i, point in enumerate(points):
            total = point[0]**2 + point[1]**2
            if total in rank:
                rank[total].append(i)
            else:
                rank[total] = [i]

        result = []
        ranked = sorted(rank.keys()) # not sorted
        count = k
        for dist in ranked:
            lst = rank[dist]
            for x in lst:
                result.append(points[x])
                # print(result)
                count-=1
            if count == 0:
                return result
        # initial (10mins)
        # debug (5mins)
# @lc code=end

