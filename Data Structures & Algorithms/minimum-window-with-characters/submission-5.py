class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        if len(s) < len(t):
            return ""

        countT = {}
        countW = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have = 0
        need = len(countT)
        respos = [-1, -1]
        resLen = len(s) + 1
        l = 0

        for r in range(len(s)):
            countW[s[r]] = countW.get(s[r], 0) + 1
            if s[r] in countT and countW[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if ((r - l) + 1) < resLen:
                    resLen = ((r - l) + 1)
                    respos = [l, r]
                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = respos
        if resLen < len(s) + 1:
            return s[l : r + 1]
        else:
            return ""

