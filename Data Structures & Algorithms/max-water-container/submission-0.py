class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_capacity = 0
        while l < r:
            curr_capacity = abs(r - l) * min(heights[r], heights[l])
            if curr_capacity > max_capacity:
                max_capacity = curr_capacity
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_capacity
            
