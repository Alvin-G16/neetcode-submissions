class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        seen = set()
        maxLength = 0

        if len(s) == 0:
            return maxLength
        if len(s) == 1:
            maxLength = 1
            return maxLength
        
        seen.add(s[l])
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            currentMax = (r - l) + 1
            maxLength = max(currentMax, maxLength)
            r += 1
        return maxLength