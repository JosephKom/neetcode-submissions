class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            exists = self.binarySearch(matrix[i], target, 0, cols - 1)
            if exists != -1:
                return True
        return False


    def binarySearch(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, right)
        else:
            return self.binarySearch(nums, target, left, mid - 1)
        
        