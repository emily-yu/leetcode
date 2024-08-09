class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        leftidx, rightidx = 0, len(numbers) - 1

        while leftidx < rightidx:
            total = numbers[leftidx] + numbers[rightidx]
            print(numbers[leftidx], numbers[rightidx], total)
            if target == total: 
                return [leftidx + 1, rightidx + 1] # +1 adjust for indexes
            elif target > total:
                leftidx += 1
            else:
                rightidx -= 1
        return None

