class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        # treat 2d matrix as 1d list
        left = 0
        right = rows * cols -1
        while left <= right:
            mid = left + (right-left)//2
            mid_val = matrix[mid//cols][mid%cols]

            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid-1
            else:
                left = mid + 1
        return False