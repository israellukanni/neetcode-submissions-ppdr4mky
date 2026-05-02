class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0

        l,r = 0, len(heights)-1
        water = 0 

        while l < r:
            if heights[l] < heights[r]:
                area = min(heights[l],heights[r]) * (r-l)
                water = max(water,area)
                l += 1
            else:
                area = min(heights[l],heights[r]) * (r-l)
                water = max(water,area)
                r -= 1
        return water