class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # compute flat length
        flattened_len = 0
        for row in matrix:
            flattened_len += len(row)
        print(flattened_len)

        def get_flattened_elem(idx):
            row_len = len(matrix[0]) # a row
            # print(row_len)
            elem = matrix[idx // row_len][idx % row_len]
            return elem
        
        # standard bst algorithm
        start, end = 0, flattened_len - 1
        middle_elem = None
        while start <= end: 
            middle = start + (end - start) // 2
            middle_elem = get_flattened_elem(middle)
            # print(middle_elem)

            if target == middle_elem:
                return True
            elif target < middle_elem:
                end = middle - 1
            elif target > middle_elem: 
                start = middle + 1
        
        return False
        # return get_flattened_elem(4)