class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                if maxLeft - height[l] < 0:
                    res += 0
                else:
                    res += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                if maxRight - height[r] < 0:
                    res += 0
                else:
                    res += maxRight - height[r]
                maxRight = max(maxRight, height[r])
        return res




