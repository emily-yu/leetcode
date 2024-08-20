class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorteds1 = sorted(list(s1)) # compare with substr sorted
        for idx in range(0, len(s2) - len(s1) + 1): # start index 2 until end
            sorteds2 = sorted(s2[idx: idx + len(s1)])
            if sorteds2 == sorteds1: 
                return True
        return False

            