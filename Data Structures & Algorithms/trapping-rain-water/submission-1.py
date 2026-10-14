class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        water_stored = 0
        max_left = 0
        max_right = 0

        while l < r:
            if height[l] <= height[r]:
                curr_water = max_left - height[l]
                if curr_water > 0:
                    water_stored += curr_water
                max_left = max(max_left, height[l])
                l += 1
            else:
                curr_water = max_right - height[r]
                if curr_water > 0:
                    water_stored += curr_water
                max_right = max(max_right, height[r])
                r -= 1
        return water_stored

        



            


