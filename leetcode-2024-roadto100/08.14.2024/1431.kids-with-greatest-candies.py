class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # if you gave the kid all candies, r they the greatest?
        s = sorted(candies)
        # check if adding makes greater than right
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= s[len(candies)-1]:
                candies[i] = True
            else:
                candies[i] = False
        return candies
