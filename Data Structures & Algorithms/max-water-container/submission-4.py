class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        globalMax = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] > heights[r]:
                r -= 1
                currentMax = min(heights[l], heights[r]) * (r - l)
                globalMax = max(currentMax, globalMax)
                continue
            if heights[l] < heights[r]:
                l += 1
                currentMax = min(heights[l], heights[r]) * (r - l)
                globalMax = max(currentMax, globalMax)
                continue
            if heights[l] == heights[r]:
                if heights[l + 1] > heights[r - 1]:
                    l += 1
                r -= 1
                currentMax = min(heights[l], heights[r]) * (r - l)
                globalMax = max(currentMax, globalMax)
                continue
        return globalMax