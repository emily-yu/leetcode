# arrays & strings

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1: return len(position)

        count = 0
        idxs = set([i for i in range(0, len(position))])
        print(idxs)
        # while len(idxs) > 0:
        while len(idxs) > 0:
            greaterthanvals = []
            # greaterthanidx = set() # remaining indx
            for i in range(len(position)):
                position[i] += speed[i]
                if i in idxs and position[i] >= target:
                    greaterthanvals.append(position[i])
                    idxs.remove(i)
            
            # check number of unique elemnts > target
            uniq = set(greaterthanvals)
            count += len(uniq)

            print(count, position, uniq, idxs)
        return count

            