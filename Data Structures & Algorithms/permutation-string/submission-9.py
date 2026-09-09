class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = len(s1) - 1
        countS1 = {}

        for s in s1:
            countS1[s] = countS1.get(s, 0) + 1
        
        while r < len(s2):
            countW = {}
            for i in range(l, r + 1):
                countW[s2[i]] = countW.get(s2[i], 0) + 1
            if countS1 == countW:
                return True
            else:
                l += 1
                r += 1
                continue
        return False