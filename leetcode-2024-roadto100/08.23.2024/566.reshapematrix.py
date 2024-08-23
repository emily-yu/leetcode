class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        # edge case
        # if r x c < len(mat): then just return mat
        count = 0
        for row in mat:
            for elem in row:
                count += 1
        if count != (r*c):
            return mat

        result, reshaped = [], []
        for row in mat:
            for elem in row:
                if len(reshaped) < c:
                    reshaped.append(elem)
                else:
                    result.append(reshaped)
                    reshaped = [elem]
        if len(reshaped) == c:
            result.append(reshaped)
        return result
